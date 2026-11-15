from collections.abc import Iterable


def _count_team_victories(
    matches: Iterable[dict],
    team: str,
) -> dict[str, int]:
    victories = {
        "home": 0,
        "away": 0,
    }

    for match in matches:
        if match["HomeTeam"] == team and match["FTR"] == "H":
            victories["home"] += 1

        if match["AwayTeam"] == team and match["FTR"] == "A":
            victories["away"] += 1

    return victories


def count_team_victories(matches: Iterable[dict], team: str) -> int:
    victories = _count_team_victories(matches, team)

    return victories["away"] + victories["home"]


def count_team_home_victories(
    matches: Iterable[dict],
    team: str,
) -> int:
    return _count_team_victories(matches, team)["home"]


def count_team_away_victories(
    matches: Iterable[dict],
    team: str,
) -> int:
    return _count_team_victories(matches, team)["away"]
