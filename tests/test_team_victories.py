from datetime import date

from premier_league_predict.football_analysis import (
    count_team_victories,
    count_team_home_victories,
)


def test_count_team_victories() -> None:
    matches = [
        {
            "Date": date(2025, 8, 16),
            "HomeTeam": "Liverpool",
            "AwayTeam": "Bournemouth",
            "FTHG": 4,
            "FTAG": 2,
            "FTR": "H",
        },
        {
            "Date": date(2025, 8, 24),
            "HomeTeam": "Arsenal",
            "AwayTeam": "Liverpool",
            "FTHG": 1,
            "FTAG": 2,
            "FTR": "A",
        },
        {
            "Date": date(2025, 9, 2),
            "HomeTeam": "Chelsea",
            "AwayTeam": "Liverpool",
            "FTHG": 1,
            "FTAG": 1,
            "FTR": "D",
        },
        {
            "Date": date(2025, 9, 10),
            "HomeTeam": "Everton",
            "AwayTeam": "Liverpool",
            "FTHG": 1,
            "FTAG": 0,
            "FTR": "H",
        },
    ]

    assert count_team_victories(matches, "Liverpool") == 2


def test_count_team_home_victories() -> None:
    matches = [
        {
            "Date": date(2025, 8, 16),
            "HomeTeam": "Liverpool",
            "AwayTeam": "Bournemouth",
            "FTHG": 4,
            "FTAG": 2,
            "FTR": "H",
        },
        {
            "Date": date(2025, 8, 24),
            "HomeTeam": "Arsenal",
            "AwayTeam": "Liverpool",
            "FTHG": 1,
            "FTAG": 2,
            "FTR": "A",
        },
        {
            "Date": date(2025, 9, 10),
            "HomeTeam": "Liverpool",
            "AwayTeam": "Chelsea",
            "FTHG": 1,
            "FTAG": 2,
            "FTR": "A",
        },
    ]

    assert count_team_home_victories(matches, "Liverpool") == 1
