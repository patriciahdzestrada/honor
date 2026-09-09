import pandas as pd

#from src.etl import tablas
#from src.medical import age
#from src.medical import adicion
#from src.medical import group
from src.etl_ratings import clean_raw_ratings
from src.etl_ratings import get_song_average_ratings

"""
def test_tablas():
    resultado = tablas(3)

    # Validación automática
    assert resultado == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

    # Reporte
    df = pd.DataFrame({"resultado": resultado})
    df.to_csv("data/resultado_tabla.csv", index=False)
"""
"""
def test_age():
    edad_valida = age()
    aplicables=adicion()
    agrupado=group()
    assert len(edad_valida) > 0
    assert len(aplicables) > 0
   

    # Guardar el DataFrame filtrado
    edad_valida.to_csv("data/edad_valida.csv", index=False)
    aplicables.to_csv("data/aplicables.csv", index=False)
    agrupado.to_csv("data/conteo.csv", index=False)

"""
df = pd.read_csv("data/raw_ratings.csv")
raw_ratings = df.to_dict(orient="records")


def test_rating():

    print("\nRAW:", raw_ratings)

    cleaned = clean_raw_ratings(raw_ratings)

    print("CLEANED:", cleaned)

    average = get_song_average_ratings(cleaned)

    assert len(cleaned) == 3

    cleaned_df = pd.DataFrame(cleaned)

    cleaned_df.to_csv("data/cleaned.csv", index=False)
    average.to_csv("data/average.csv", index=False)

