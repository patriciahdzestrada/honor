from src.etl import tablas

def test_tablas():
    resultado = tablas(3)

    # Validación automática
    assert resultado == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

    # Reporte
    df = pd.DataFrame(resultado, columns=["resultado"])
    df.to_csv("data/resultado_tabla.csv", index=False)