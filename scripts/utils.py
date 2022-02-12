import re
from typing import Any

import pandas as pd


def format_cell(data: Any) -> str:
    if pd.isna(data):
        return ""

    if not isinstance(data, str):
        return str(data)

    return data.strip()


def strip_ref(data: Any) -> str:
    if not isinstance(data, str):
        data = format_cell(data)

    return re.sub(r"\[[0-9A-Za-z]+\]", "", data).strip()
