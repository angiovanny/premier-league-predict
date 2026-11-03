from collections.abc import Iterable


def count_team_victories(matches: Iterable[dict], team: str) -> int:
    victories = 0

    for match in matches:
        if match["HomeTeam"] == team and match["FTR"] == "H":
            victories += 1

        if match["AwayTeam"] == team and match["FTR"] == "A":
            victories += 1

    return victories
