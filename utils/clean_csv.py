import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean DataFrame:
    - Remove duplicates
    - Handle null values
    - Format dates
    - Format floats to 2 decimals
    """

    df = df.copy()

    df.drop_duplicates(inplace=True)
    if "nombre" in df.columns:
        df["nombre"] = df["nombre"].str.upper().str.strip()
    if "fecha" in df.columns:
        df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

    df.fillna({
        "precio": 0,
        "total": 0
    }, inplace=True)

    # Redondear floats
    for col in ["precio", "total"]:
        if col in df.columns:
            df[col] = df[col].astype(float).round(2)

    return df
