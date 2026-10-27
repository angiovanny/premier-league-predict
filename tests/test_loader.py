import pytest

from premier_league_predict.loader import load_season

def test_load_season(tmp_path) -> None:
    csv_path = tmp_path / "season_2025.csv"

    csv_path.write_text(
        "Date,HomeTeam,AwayTeam,FTHG,FTAG,FTR\n"
        "16/08/2025,Liverpool,Bournemouth,4,2,H\n"
        "17/08/2025,Aston Villa,Newcastle,0,0,D"
    )

    results = load_season(csv_path)

    assert isinstance(results, list)
    assert len(results) == 2
    assert results[0]["Date"] == "16/08/2025"
    assert results[0]["HomeTeam"] == "Liverpool"


def test_csv_missing_ftag_column_is_invalid(tmp_path) -> None:
    csv_path = tmp_path / "season_2025.csv"

    csv_path.write_text(
        "Date,HomeTeam,AwayTeam,FTHG,FTR\n"
        "16/08/2025,Liverpool,Bournemouth,4,H\n"
        "17/08/2025,Aston Villa,Newcastle,0,D"
    )

    with pytest.raises(ValueError, match="CSV structure failed: missing required columns: FTAG"):
        load_season(csv_path)


def test_csv_with_multiple_missing_columns_is_invalid(tmp_path) -> None:
    csv_path = tmp_path / "season_2025.csv"

    csv_path.write_text(
        "Date,HomeTeam,FTHG,FTR\n"
        "16/08/2025,Liverpool,4,H\n"
        "17/08/2025,Aston Villa,0,D"
    )

    with pytest.raises(ValueError, match="CSV structure failed: missing required columns: AwayTeam, FTAG"):
        load_season(csv_path)
