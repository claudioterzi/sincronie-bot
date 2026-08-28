"""Utilità Markdown per SincronieBot."""

from __future__ import annotations

import re

_SPECIAL = r"\_*[]()~`>#+-=|{}.!"


def escape(text: str) -> str:
    return re.sub(r"([" + re.escape(_SPECIAL) + r"])", r"\\\1", text or "")
