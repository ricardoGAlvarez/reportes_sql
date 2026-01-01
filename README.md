# ETL Pipeline: Análisis de Retail 

Este proyecto implementa un flujo de datos (ETL) completo utilizando **Python** para el procesamiento y **PostgreSQL** para el almacenamiento y análisis.

## 🚀 Estructura del Proyecto
- `data/`: Archivos CSV de origen (Ventas, Productos, Sucursales).
- `utils/clean_csv.py`: Lógica de limpieza y normalización con Pandas.
- `utils/export_to_sql.py`: Módulo de conexión y carga a base de datos relacional.
- `main.py`: Orquestador del pipeline.

## 🛠️ Tecnologías utilizadas
- **Python 3.x** (Pandas, SQLAlchemy).
- **PostgreSQL**.
- **Lógica SQL** (Views, Joins, Agregaciones).

## 📊 Análisis de Datos
Se creó una Vista (`REPORTE_MAESTRO`) que consolida la información para responder preguntas de negocio como:
- Recaudación total por ciudad (Palpalá, San Salvador, Salta, etc.).
- Productos más vendidos por categoría.
- Evolución temporal de ingresos.