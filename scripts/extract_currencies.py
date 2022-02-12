import json
from pathlib import Path

import pandas
import requests

from .utils import format_cell

OUT_FILE = Path(__file__).parent.parent / "data/json/currencies.json"


def get_html_content():
    url = "https://justforex.com/education/currencies"
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def main():
    dataframe = pandas.read_html(get_html_content(), header=0, attrs={"id": "js-table-currencies"})[0]
    data = []

    for item in dataframe.itertuples():
        symbol = format_cell(item[2])

        if symbol:
            data.append(
                {
                    "iso_4217_code": format_cell(item[1]),
                    "iso_4217_numeric_code": format_cell(item[3]),
                    "name": format_cell(item[4]),
                    "symbol": symbol,
                }
            )

    with OUT_FILE.open("w+") as file:
        file.write(json.dumps(data, indent=2))
        file.write("\n")


if __name__ == "__main__":
    main()
