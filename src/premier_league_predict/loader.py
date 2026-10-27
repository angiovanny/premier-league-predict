import csv
from pathlib import Path


REQUIRED_COLUMNS = {
    "Date",
    "HomeTeam",
    "AwayTeam",
    "FTHG",
    "FTAG",
    "FTR",
}


def load_season(season_path: str | Path) -> list[dict]:
    season_path = Path(season_path)
    results: list[dict] = []

    with season_path.open() as file:
        reader = csv.DictReader(file)

        missing_columns = REQUIRED_COLUMNS - set(reader.fieldnames)

        if missing_columns:
            raise ValueError(
                f'CSV structure failed: missing required columns: {", ".join(sorted(missing_columns))}'
            )

        for row in reader:
            results.append(row)

    return results
