from premier_league_predict.transform import transform_match


def test_transform_fthg_and_ftag_to_int() -> None:
    raw_match = {
        "Date": "16/08/2025",
        "HomeTeam": "Liverpool",
        "AwayTeam": "Bournemouth",
        "FTHG": "4",
        "FTAG": "2",
        "FTR": "H",
    }

    result = transform_match(raw_match)

    assert isinstance(result["FTHG"], int)
    assert result["FTHG"] == 4
    assert raw_match["FTHG"] == "4"

    assert isinstance(result["FTAG"], int)
    assert result["FTAG"] == 2
    assert raw_match["FTAG"] == "2"
