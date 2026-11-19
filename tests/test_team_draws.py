from datetime import date

from premier_league_predict.football_analysis import count_team_draws

def test_count_team_draws() -> None:
    matches = [
        {
            "Date": date(2025, 8, 16),
            "HomeTeam": "Bournemouth",
            "AwayTeam": "Liverpool",
            "FTHG": 2,
            "FTAG": 2,
            "FTR": "D",
        },
        {
            "Date": date(2025, 8, 24),
            "HomeTeam": "Liverpool",
            "AwayTeam": "Arsenal",
            "FTHG": 1,
            "FTAG": 1,
            "FTR": "D",
        },
        {
            "Date": date(2025, 9, 10),
            "HomeTeam": "Everton",
            "AwayTeam": "Liverpool",
            "FTHG": 2,
            "FTAG": 3,
            "FTR": "A",
        },
        {
            "Date": date(2025, 9, 18),
            "HomeTeam": "Chelsea",
            "AwayTeam": "Liverpool",
            "FTHG": 5,
            "FTAG": 2,
            "FTR": "H",
        },
        {
            "Date": date(2025, 9, 26),
            "HomeTeam": "Chelsea",
            "AwayTeam": "Everton",
            "FTHG": 2,
            "FTAG": 2,
            "FTR": "D",
        },
    ]

    assert count_team_draws(matches, "Liverpool") == 2
