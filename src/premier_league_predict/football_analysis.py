from collections.abc import Iterable


def _get_team_statistics(
    matches: Iterable[dict],
    team: str,
) -> dict[str, int]:
    statistics = {
        "home_victories": 0,
        "away_victories": 0,
        "losses": 0,
        "draws": 0,
    }

    for game in matches:
        if game["HomeTeam"] != team and game["AwayTeam"] != team:
            continue

        match game["FTR"]:
            case "H":
                if game["HomeTeam"] == team:
                    statistics["home_victories"] += 1
                else:
                    statistics["losses"] += 1

            case "A":
                if game["HomeTeam"] == team:
                    statistics["losses"] += 1
                else:
                    statistics["away_victories"] += 1

            case "D":
                statistics["draws"] += 1

    return statistics


def count_team_victories(matches: Iterable[dict], team: str) -> int:
    statistics = _get_team_statistics(matches, team)

    return statistics["away_victories"] + statistics["home_victories"]


def count_team_home_victories(
    matches: Iterable[dict],
    team: str,
) -> int:
    return _get_team_statistics(matches, team)["home_victories"]


def count_team_away_victories(
    matches: Iterable[dict],
    team: str,
) -> int:
    return _get_team_statistics(matches, team)["away_victories"]


def count_team_draws(
    matches: Iterable[dict],
    team: str,
) -> int:
    return _get_team_statistics(matches, team)["draws"]


def count_team_losses(
    matches: Iterable[dict],
    team: str,
) -> int:
    return _get_team_statistics(matches, team)["losses"]
