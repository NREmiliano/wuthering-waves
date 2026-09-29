import os
import json
import pandas as pd

def buscar_archivo(nombre_archivo):
    """Busca un archivo recursivamente en el proyecto o en la carpeta de datos."""
    for root, dirs, files in os.walk("."):
        if nombre_archivo in files:
            return os.path.join(root, nombre_archivo)
    if os.path.exists("../WutheringWaves_Data"):
        for root, dirs, files in os.walk("../WutheringWaves_Data"):
            if nombre_archivo in files:
                return os.path.join(root, nombre_archivo)
    return None

def analizar_armas():
    print("=== MÓDULO DE ARMAS: BUSCANDO METADATOS ===")
    
    # Buscamos de forma inteligente archivos relacionados con armas en BinData
    ruta_arma_json = None
    for root, dirs, files in os.walk("WutheringWaves_Data"):
        for file in files:
            if "weapon" in file.lower() and file.endswith(".json"):
                ruta_arma_json = os.path.join(root, file)
                break
        if ruta_arma_json:
            break
            
    if not ruta_arma_json and os.path.exists("../WutheringWaves_Data"):
        for root, dirs, files in os.walk("../WutheringWaves_Data"):
            for file in files:
                if "weapon" in file.lower() and file.endswith(".json"):
                    ruta_arma_json = os.path.join(root, file)
                    break
            if ruta_arma_json:
                break

    if not ruta_arma_json:
        print("❌ No se encontró ningún archivo JSON relacionado con armas en la estructura de datos.")
        return

    print(f"✔️ Archivo de armas localizado: {ruta_arma_json}")

    with open(ruta_arma_json, 'r', encoding='utf-8') as f:
        armas_data = json.load(f)

    if isinstance(armas_data, list) and len(armas_data) > 0:
        print(f"Total de registros de armas encontrados: {len(armas_data)}\n")
        print("Muestra de los primeros 3 registros de armas:")
        for item in armas_data[:3]:
            print(item)
    elif isinstance(armas_data, dict):
        print(f"El archivo contiene un diccionario con {len(armas_data)} claves principales.")
        muestra = list(armas_data.values())[:3]
        for item in muestra:
            print(item)

if __name__ == "__main__":
    analizar_armas()