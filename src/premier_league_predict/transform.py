from datetime import datetime


def transform_match(raw_match: dict) -> dict:
    result = raw_match.copy()

    result["FTHG"] = int(result["FTHG"])
    result["FTAG"] = int(result["FTAG"])

    result["Date"] = datetime.strptime(result["Date"], "%d/%m/%Y").date()

    return result
