from datetime import date

from premier_league_predict.football_analysis import (
    count_team_away_victories,
    count_team_home_victories,
    count_team_victories,
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


def test_count_team_away_victories() -> None:
    matches = [
        {
            "Date": date(2025, 8, 16),
            "HomeTeam": "Bournemouth",
            "AwayTeam": "Liverpool",
            "FTHG": 2,
            "FTAG": 4,
            "FTR": "A",
        },
        {
            "Date": date(2025, 8, 24),
            "HomeTeam": "Liverpool",
            "AwayTeam": "Arsenal",
            "FTHG": 2,
            "FTAG": 1,
            "FTR": "H",
        },
        {
            "Date": date(2025, 9, 10),
            "HomeTeam": "Everton",
            "AwayTeam": "Liverpool",
            "FTHG": 2,
            "FTAG": 2,
            "FTR": "D",
        },
        {
            "Date": date(2025, 9, 18),
            "HomeTeam": "Chelsea",
            "AwayTeam": "Liverpool",
            "FTHG": 5,
            "FTAG": 2,
            "FTR": "H",
        },
    ]

    assert count_team_away_victories(matches, "Liverpool") == 1


def test_count_team_victories_with_generator() -> None:
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
            "FTHG": 2,
            "FTAG": 2,
            "FTR": "D",
        },
    ]

    matches_generator = (match for match in matches)

    assert count_team_victories(matches_generator, "Liverpool") == 2
