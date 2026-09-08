import pandas as pd

#from src.etl import tablas
from src.medical import age


"""
def test_tablas():
    resultado = tablas(3)

    # Validación automática
    assert resultado == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

    # Reporte
    df = pd.DataFrame({"resultado": resultado})
    df.to_csv("data/resultado_tabla.csv", index=False)
"""

def test():
    edad_valida= age()
    assert len(edad_valida) > 0

    #Guardar Dataframe
    df=pd.DataFrame({"edad_valida": edad_valida})
    df.to_csv("data/edad_valida.csv", index=False) 
    
