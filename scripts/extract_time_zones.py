import json
import re
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

from .utils import format_cell

OUT_FILE = Path(__file__).parent.parent / "data/json/time_zones.json"


def make_offsets(offset: str):
    numeric_part = None
    sep = None
    hour = None
    minute = None

    if "/" in offset:
        offset = offset.split("/")[0].strip()

    if "+" in offset:
        numeric_part = offset.split("+")[-1]
        sep = "+"
    elif "-" in offset:
        numeric_part = offset.split("-")[-1]
        sep = "-"
    else:
        numeric_part = "0"
        sep = "+"

    if ":" in numeric_part:
        hour, minute = numeric_part.split(":")
    else:
        hour, minute = numeric_part, "0"

    offset_dt = datetime(day=1, month=1, year=2000, hour=int(hour, 10), minute=int(minute, 10))
    numeric_part = offset_dt.strftime("%H:%M")
    numeric_part_no_colon = offset_dt.strftime("%H%M")
    minutes = round(timedelta(hours=int(hour, 10), minutes=int(minute, 10)).total_seconds() / 60)

    if sep == "-":
        minutes *= -1

    return (
        f"UTC {sep}{numeric_part}",
        f"{sep}{numeric_part}",
        f"{sep}{numeric_part_no_colon}",
        minutes,
    )


def format_name(name: str):
    return re.sub(r"[A-Z]+\s+\u2013.+", "", name).strip() if "\u2013" in name else name


def main():
    url = "https://www.timeanddate.com/time/zones/"
    dataframe = pd.read_html(url, header=0)[0]
    data = []

    for item in dataframe.itertuples():
        abbr = format_cell(item[1])
        name = format_name(format_cell(item[2]))
        offset_display_text, offset_text, offset_text_clean, offset_minutes = make_offsets(format_cell(item[4]))

        data.append(
            {
                "abbreviation": abbr,
                "name": name,
                "offset_display_text": offset_display_text,
                "offset_text": offset_text,
                "offset_text_clean": offset_text_clean,
                "offset_minutes": offset_minutes,
            }
        )

    with OUT_FILE.open("w+") as file:
        file.write(json.dumps(data, indent=2))
        file.write("\n")


if __name__ == "__main__":
    main()
