from datetime import date

from premier_league_predict.football_analysis import count_team_losses


def test_count_team_losses() -> None:
    matches = [
        {
            "Date": date(2025, 8, 16),
            "HomeTeam": "Liverpool",
            "AwayTeam": "Arsenal",
            "FTHG": 1,
            "FTAG": 3,
            "FTR": "A",
        },
        {
            "Date": date(2025, 8, 24),
            "HomeTeam": "Chelsea",
            "AwayTeam": "Liverpool",
            "FTHG": 2,
            "FTAG": 0,
            "FTR": "H",
        },
        {
            "Date": date(2025, 9, 10),
            "HomeTeam": "Liverpool",
            "AwayTeam": "Everton",
            "FTHG": 3,
            "FTAG": 1,
            "FTR": "H",
        },
        {
            "Date": date(2025, 9, 18),
            "HomeTeam": "Bournemouth",
            "AwayTeam": "Liverpool",
            "FTHG": 1,
            "FTAG": 1,
            "FTR": "D",
        },
        {
            "Date": date(2025, 9, 26),
            "HomeTeam": "Arsenal",
            "AwayTeam": "Chelsea",
            "FTHG": 0,
            "FTAG": 2,
            "FTR": "A",
        },
        {
            "Date": date(2025, 10, 3),
            "HomeTeam": "Everton",
            "AwayTeam": "Liverpool",
            "FTHG": 0,
            "FTAG": 2,
            "FTR": "A",
        },
    ]

    assert count_team_losses(matches, "Liverpool") == 2