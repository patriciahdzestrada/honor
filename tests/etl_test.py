import pandas as pd

#from src.etl import tablas
from src.medical import age
from src.medical import adicion


"""
def test_tablas():
    resultado = tablas(3)

    # Validación automática
    assert resultado == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

    # Reporte
    df = pd.DataFrame({"resultado": resultado})
    df.to_csv("data/resultado_tabla.csv", index=False)
"""

def test_age():
    edad_valida = age()
    aplicables=adicion()
    assert len(edad_valida) > 0

    # Guardar el DataFrame filtrado
    edad_valida.to_csv("data/edad_valida.csv", index=False)
    aplicables.to_csv("data/aplicables.csv", index=False)

