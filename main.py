import pandas as pd
from utils.clean_csv import clean_data  # si la función está en clean.py
from utils.export_to_sql import export_to_sql  # si la función está en export_to_sql.py
def main():
    df_ventas = pd.read_csv("data/ventas.csv")
    df_productos = pd.read_csv("data/productos.csv")
    df_sucursales = pd.read_csv("data/sucursales.csv")
    df_cleaned_ventas = clean_data(df_ventas)
    df_cleaned_productos = clean_data(df_productos)
    df_cleaned_sucursales = clean_data(df_sucursales)
    export_to_sql(df_cleaned_ventas, "ventas")
    export_to_sql(df_cleaned_productos, "productos")
    export_to_sql(df_cleaned_sucursales, "sucursales")

if __name__ == "__main__":
    main()
