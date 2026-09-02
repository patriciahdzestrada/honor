import os
import sys
import pandas as pd

# Permite importar desde la carpeta /src
sys.path.append(os.path.abspath("src"))

from etl_ratings import clean_raw_ratings, ejecutar_etl_ratings, get_song_average_ratings


def test_clean_raw_ratings():
    raw_ratings = [
        {"user_id": "u1", "song_id": "s101", "rating": 5},
        {"user_id": "u2", "song_id": "s102", "rating": 12},  # Calificación inválida (> 5)
        {"user_id": "u1", "song_id": "s101", "rating": 5},   # Duplicado
        {"user_id": "u3", "rating": 4},                     # Incompleto
        {"user_id": "u4", "song_id": "s101", "rating": 4},   # Válido
        {"user_id": "u1", "song_id": "s102", "rating": 2},   # Válido
        {"user_id": "u2", "song_id": "s102", "rating": 0},   # Calificación inválida (< 1)
    ]

    cleaned = clean_raw_ratings(raw_ratings)

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


def test_ejecutar_etl_integracion(tmp_path):
    # Generar un CSV temporal para la prueba
    input_file = tmp_path / "raw_ratings.csv"
    output_file = tmp_path / "resultado.csv"

    df_test = pd.DataFrame([
        {"user_id": "u1", "song_id": "s101", "rating": 5},
        {"user_id": "u4", "song_id": "s101", "rating": 4},
        {"user_id": "u2", "song_id": "s102", "rating": 10},  # Inválido
    ])
    df_test.to_csv(input_file, index=False)

    # Ejecutar pipeline
    ejecutar_etl_ratings(str(input_file), str(output_file))

    # Validar generación del CSV final
    assert os.path.exists(output_file)

    df_out = pd.read_csv(output_file)
    assert "average_rating" in df_out.columns
    assert df_out[df_out["song_id"] == "s101"]["average_rating"].iloc[0] == 4.5