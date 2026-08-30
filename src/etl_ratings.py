import os
import pandas as pd


def clean_raw_ratings(raw_ratings: list) -> list:
    """
    Filtra registros incompletos, ratings fuera de rango (1-5)
    y duplica combinaciones de (user_id, song_id).
    """
    seen_pairs = set()
    cleaned_ratings = []
    requeridos = ["user_id", "song_id", "rating"]

    for raw in raw_ratings:
        if all(campo in raw for campo in requeridos):
            if 1 <= raw["rating"] <= 5:
                pair = (raw["user_id"], raw["song_id"])
                if pair not in seen_pairs:
                    cleaned_ratings.append(raw)
                    seen_pairs.add(pair)

    return cleaned_ratings


def get_song_average_ratings(ratings: list) -> pd.DataFrame:
    """
    Calcula el promedio de rating por canción y retorna un DataFrame.
    """
    calf_promedio = {}

    for cal in ratings:
        song_id = cal["song_id"]
        prom = cal["rating"]

        if song_id in calf_promedio:
            calf_promedio[song_id].append(prom)
        else:
            calf_promedio[song_id] = [prom]

    promedios = {
        song: sum(puntuaciones) / len(puntuaciones)
        for song, puntuaciones in calf_promedio.items()
    }

    df_promedios = pd.DataFrame(
        list(promedios.items()), columns=["song_id", "average_rating"]
    )

    return df_promedios


def ejecutar_etl_ratings(input_path: str, output_path: str) -> pd.DataFrame:
    """
    Orquestador principal del proceso ETL.
    """
    # 1. Extract (soporta CSV o carga directa si ya existe)
    df_raw = pd.read_csv(input_path)
    raw_ratings = df_raw.to_dict(orient="records")

    # 2. Transform
    cleaned = clean_raw_ratings(raw_ratings)
    df_result = get_song_average_ratings(cleaned)

    # 3. Load
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_result.to_csv(output_path, index=False)

    return df_result


if __name__ == "__main__":
    ejecutar_etl_ratings("data/raw_ratings.csv", "data/resultado_promedios.csv")