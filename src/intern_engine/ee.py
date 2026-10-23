"""Conservative title-only EE scope, isolated from upstream's software rules.

Generic systems/test/validation roles require an explicit electrical signal.
Descriptions mentioning an EE degree alone do not establish the job's scope.
"""

import re


def _pattern(words: str) -> re.Pattern:
    return re.compile(r"\b(?:" + words + r")\b", re.IGNORECASE)


_EXCLUDE = _pattern(
    r"sales|marketing|recruit\w*|accounting|legal|human resources|unpaid|"
    r"product manag\w*|supply chain|public relations|corporate communications|"
    r"phd|ph\.d|doctoral"
)
_CATEGORIES = [
    ("Embedded & Firmware", _pattern(r"embedded|firmware")),
    ("Digital & Semiconductors", _pattern(
        r"asic|fpga|rtl|vlsi|silicon|semiconductor|physical design|"
        r"digital (?:design|verification)|design verification|"
        r"integrated circuits?|microelectronics"
    )),
    ("RF & Communications", _pattern(
        r"rf|radio frequency|microwave|antenna|wireless|"
        r"signal processing|communications? (?:systems?|engineering)"
    )),
    ("Power & Energy", _pattern(
        r"power electronics|power systems?|power engineering|"
        r"electrical power|electric (?:drives?|motors?)|"
        r"motor control|grid (?:engineering|protection)|protection and control"
    )),
    ("Circuits & Electronics", _pattern(
        r"analog|mixed[ -]signal|pcb|circuit\w*|electronics|electronic engineering"
    )),
    ("Controls & Instrumentation", _pattern(
        r"controls? (?:engineering|engineer|systems?)|instrumentation|"
        r"plc|scada|mechatronics|avionics"
    )),
    ("Electrical & Hardware", _pattern(r"electrical|hardware")),
]


def category(title: str) -> str | None:
    """Return the strongest EE title family, or None when evidence is absent."""
    if not title or _EXCLUDE.search(title):
        return None
    for label, pattern in _CATEGORIES:
        if pattern.search(title):
            return label
    return None


def is_ee(title: str) -> bool:
    return category(title) is not None
