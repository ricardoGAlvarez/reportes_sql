from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://postgres:admin@localhost:5432/mi_proyecto')

def export_to_sql(df:pd.DataFrame, table_name):
    """
    Exportar DataFrame a una tabla SQL.
    Si la tabla ya existe, se reemplaza.
    """
    try:
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Datos exportados exitosamente a la tabla '{table_name}'.")
    except Exception as e:
        print(f"Error al exportar datos a la tabla '{table_name}': {e}")
    return True