import re
from typing import Any

import pandas as pd


def format_cell(s: Any) -> str:
    if pd.isna(s):
        return ""

    if not isinstance(s, str):
        return str(s)

    return s.strip()


def strip_ref(s: Any) -> str:
    if not isinstance(s, str):
        s = format_cell(s)

    return re.sub(r"\[[0-9A-Za-z]+\]", "", s).strip()
