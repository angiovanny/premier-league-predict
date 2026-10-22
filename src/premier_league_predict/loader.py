from pathlib import Path
import csv


def load_season(season_path: str | Path) -> list[dict]:
    season_path = Path(season_path)
    results: list[dict] = []

    with season_path.open() as file:
        reader = csv.DictReader(file)

        for row in reader:
            results.append(row)

    return results
    