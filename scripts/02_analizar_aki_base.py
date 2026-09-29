import os
import pandas as pd


def analizar_aki_base():
  # Ruta del archivo CSV maestro en la carpeta clonada
  ruta_csv = "WutheringWaves_Data/aki_base.csv"

  print("=== ANÁLISIS DE AKI_BASE.CSV ===")

  if os.path.exists(ruta_csv):
    # Leemos el archivo CSV usando Pandas
    df = pd.read_csv(ruta_csv)

    print("\n--- Primeras 5 filas del archivo ---")
    print(df.head())

    print("\n--- Columnas disponibles en la base de datos ---")
    print(df.columns.tolist())
  else:
    print("El archivo aki_base.csv no se encuentra en la ruta especificada.")


if __name__ == "__main__":
  analizar_aki_base()