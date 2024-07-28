import re
import time
from typing import Any, Dict, List, Optional, Tuple

import requests
from bs4 import BeautifulSoup

from app.utils.cache import redis_lock


class GoogleScholarService:
    base_url = "https://scholar.google.com/scholar"
    meta_pattern = re.compile(r"([,\d]+) results \(([\d.]+)\s*sec\)")  # Compile the regex pattern for efficiency
    MAX_PAGE_COUNT = 100
    PAGE_SIZE = 10
    SORT_BY_DATE = "date"
    SORT_BY_RELEVANCE = "relevance"
    SORTING_CRITERIA = [SORT_BY_DATE, SORT_BY_RELEVANCE]

    @redis_lock("google-scholar-search", timeout=10)
    def search(
        self,
        query: str,
        page: int = 1,
        sorting: Optional[str] = None,
        year_max: Optional[int] = None,
        year_min: Optional[int] = None,
    ) -> Dict[str, Any]:
        if not sorting:
            sorting = self.SORT_BY_RELEVANCE

        params = {
            "as_vis": 1,  # Exclude citations.
            "hl": "en",
            "lookup": 0,
            "q": query,
            "start": (page - 1) * self.PAGE_SIZE,
        }

        if year_max:
            params["as_yhi"] = year_max

        if year_min:
            params["as_ylo"] = year_min

        if sorting == self.SORT_BY_DATE:
            params["scisbd"] = 1

        res = requests.get(self.base_url, params=params)

        res.raise_for_status()

        soup = BeautifulSoup(res.text, "lxml")

        articles = []

        gs_ab_mdw = soup.select_one("div#gs_ab_md > div.gs_ab_mdw")
        gs_ab_mdw_text = gs_ab_mdw.get_text(strip=True)

        # Use pattern.search() to find the pattern in the text
        match = self.meta_pattern.search(gs_ab_mdw_text)
        num_results = int(match.group(1).replace(",", ""))  # Extract the number of results
        took = float(match.group(2))  # Extract the time taken

        # Create the dictionary
        meta = {
            "took": took,
            "total": num_results,
        }

        # Find all article elements
        article_elements = soup.find_all("div", class_="gs_r gs_or gs_scl", attrs={"data-cid": True, "data-rp": True})

        for div in article_elements:
            data = {"id": div["data-cid"]}

            # div.gs_or_ggsm>a (href link)
            ggsm_a = div.select_one("div.gs_or_ggsm > a")
            if ggsm_a and "[PDF]" in ggsm_a.get_text(" ", strip=True):
                data["pdf_url"] = ggsm_a["href"] if ggsm_a else None
            else:
                data["pdf_url"] = None

            # div.gs_ri>h3>a (href link)
            ri_h3_a = div.select_one("div.gs_ri > h3 > a")
            data["url"] = ri_h3_a["href"]

            # div.gs_ri>h3>a (text no tags)
            for bold in ri_h3_a.find_all("b"):
                bold.replace_with(f"**{bold.get_text(' ', strip=True)}**")
            data["title"] = ri_h3_a.get_text(" ", strip=True)

            # div.gs_a (text no tags)
            gs_a = div.select_one("div.gs_a")
            data["subtitle"] = gs_a.get_text(strip=True) if gs_a else None

            # div.gs_rs (text with <b> tags)
            gs_rs = div.select_one("div.gs_rs")
            if gs_rs:
                for bold in gs_rs.find_all("b"):
                    bold.replace_with(f"**{bold.get_text(' ', strip=True)}**")

                # Replace <span class="gs_age"> tags with _text_
                for age_element in gs_rs.find_all("span", class_="gs_age"):
                    age_element.replace_with(f"_{age_element.get_text(" ", strip=True)}_")

                data["description"] = gs_rs.get_text(" ", strip=True)
            else:
                data["description"] = None

            # div.gs_fl gs_flb (a with text "Cited by N", get the N number, does not always exist, default take 0)
            gs_fl_a = div.select_one('div.gs_fl a:-soup-contains("Cited by")')
            if gs_fl_a:
                cited_by_text = gs_fl_a.get_text(" ", strip=True)
                cited_by_number = cited_by_text.split()[-1]
                data["cited_by"] = int(cited_by_number)
            else:
                data["cited_by"] = 0

            articles.append(data)

        return {
            "count": min(self.MAX_PAGE_COUNT * self.PAGE_SIZE, num_results),
            "results": articles,
            "meta": meta,
        }
