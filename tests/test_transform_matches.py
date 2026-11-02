from datetime import date

from premier_league_predict.transform import transform_matches


def test_transform_matches() -> None:
    raw_matches = [
        {
            "Date": "16/08/2025",
            "HomeTeam": "Liverpool",
            "AwayTeam": "Bournemouth",
            "FTHG": "4",
            "FTAG": "2",
            "FTR": "H",
        },
        {
            "Date": "16/08/2025",
            "HomeTeam": "Chelsea",
            "AwayTeam": "Arsenal",
            "FTHG": "2",
            "FTAG": "1",
            "FTR": "H",
        },
    ]

    result = transform_matches(raw_matches)

    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], dict)
    assert isinstance(result[1], dict)
    assert isinstance(result[0]["Date"], date)
    assert isinstance(result[0]["FTAG"], int)
    assert isinstance(result[1]["Date"], date)
    assert isinstance(result[1]["FTAG"], int)
    assert raw_matches[0]["Date"] == "16/08/2025"
    assert raw_matches[0]["FTAG"] == "2"
