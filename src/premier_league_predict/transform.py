from datetime import datetime

from collections.abc import Iterable


def transform_match(raw_match: dict) -> dict:
    result = raw_match.copy()

    result["FTHG"] = int(result["FTHG"])
    result["FTAG"] = int(result["FTAG"])

    result["Date"] = datetime.strptime(result["Date"], "%d/%m/%Y").date()

    return result


def transform_matches(raw_matches: Iterable[dict]) -> list[dict]:
    return [transform_match(match) for match in raw_matches]
