import os
import sys
import pandas as pd

# Permite importar desde la carpeta /src
sys.path.append(os.path.abspath("src"))

from etl_ratings import clean_raw_ratings, get_song_average_ratings


def test_clean_raw_ratings():
    cleaned = clean_raw_ratings("data/raw_ratings.csv")

    # Deben quedar exactamente 3 registros válidos
    assert len(cleaned) == 3
    assert cleaned == [
        {"user_id": "u1", "song_id": "s101", "rating": 5},
        {"user_id": "u4", "song_id": "s101", "rating": 4},
        {"user_id": "u1", "song_id": "s102", "rating": 2},
    ]


def test_get_song_average_ratings():
    cleaned_ratings = [
        {"user_id": "u1", "song_id": "s101", "rating": 5},
        {"user_id": "u4", "song_id": "s101", "rating": 4},
        {"user_id": "u1", "song_id": "s102", "rating": 2},
    ]

    df = get_song_average_ratings(cleaned_ratings)

    # Comprobar promedios calculados: s101 -> 4.5, s102 -> 2.0
    expected_promedios = {"s101": 4.5, "s102": 2.0}
    result_dict = dict(zip(df["song_id"], df["average_rating"]))

    assert result_dict == expected_promedios


