import os
import json
import pandas as pd

def buscar_y_vincular_stats():
    print("=== BUSCANDO Y VINCULANDO ESTADÍSTICAS BASE ===")
    
    # 1. Cargar nuestro DataFrame maestro de personajes
    processed_path = "../WutheringWaves_Data/processed/personajes_mapeados.csv" if os.path.exists("../WutheringWaves_Data") else "WutheringWaves_Data/processed/personajes_mapeados.csv"
    
    if not os.path.exists(processed_path):
        print(f"No se encontró el archivo maestro en: {processed_path}. Ejecuta primero el script anterior.")
        return
    
    df_personajes = pd.read_csv(processed_path)
    print(f"Personajes cargados desde el maestro: {len(df_personajes)}")

    # 2. Localizar la carpeta BinData
    bindata_path = "../WutheringWaves_Data/BinData" if os.path.exists("../WutheringWaves_Data") else "WutheringWaves_Data/BinData"
    
    # Busquemos archivos JSON dentro de BinData que puedan contener estadísticas o atributos (ej. "role", "property", "attribute", "grow")
    archivos_candidatos = []
    if os.path.exists(bindata_path):
        for root, dirs, files in os.walk(bindata_path):
            for file in files:
                if file.endswith(".json"):
                    # Filtramos por palabras clave comunes en juegos para stats de personajes
                    lower_file = file.lower()
                    if any(k in lower_file for k in ["prop", "attribute", "growth", "level", "stat", "role"]):
                        archivos_candidatos.append(os.path.join(root, file))

    print(f"Se encontraron {len(archivos_candidatos)} archivos candidatos relacionados con atributos/roles.")

    # 3. Inspeccionar las estructuras de los archivos candidatos para hallar las estadísticas
    # Vamos a buscar archivos que contengan propiedades de combate vinculadas al ID del personaje
    estadisticas_encontradas = []
    
    for ruta_archivo in archivos_candidatos:
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list) and len(data) > 0:
                    muestra = data[0]
                    if isinstance(muestra, dict):
                        # Buscamos claves que suelan representar IDs de personajes y estadísticas base
                        claves = muestra.keys()
                        # Verificamos si alguna clave coincide o se relaciona con IDs y atributos numéricos
                        if any(c in str(claves).lower() for c in ["hp", "atk", "attack", "def", "grow", "property"]):
                            print(f"\n[CANDIDATO FUERTE] Archivo: {os.path.basename(ruta_archivo)}")
                            print(f"Claves disponibles: {list(claves)[:10]}")
                            # Podríamos extraer una muestra para analizarla
        except Exception:
            pass

if __name__ == "__main__":
    buscar_y_vincular_stats()