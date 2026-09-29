import os
import json

def buscar_stats_exactas():
    print("=== BÚSQUEDA QUIRÚRGICA DE ESTADÍSTICAS DE PERSONAJES ===")
    
    bindata_path = "../WutheringWaves_Data/BinData" if os.path.exists("../WutheringWaves_Data") else "WutheringWaves_Data/BinData"
    
    hallazgos = []
    
    if os.path.exists(bindata_path):
        for root, dirs, files in os.walk(bindata_path):
            for file in files:
                lower_file = file.lower()
                # Buscamos archivos que pertenezcan al ecosistema de roles/personajes
                if any(k in lower_file for k in ["role", "character", "hero"]):
                    ruta = os.path.join(root, file)
                    try:
                        with open(ruta, 'r', encoding='utf-8') as f:
                            datos = json.load(f)
                            if isinstance(datos, list) and len(datos) > 0:
                                muestra = datos[0]
                                if isinstance(muestra, dict):
                                    claves = list(muestra.keys())
                                    claves_str = str(claves).lower()
                                    
                                    # Filtramos los que tengan propiedades de combate o niveles de crecimiento
                                    if any(term in claves_str for term in ["atk", "lifemax", "property", "grow", "attr", "level"]):
                                        hallazgos.append((file, claves))
                    except Exception:
                        pass

    print(f"\nSe encontraron {len(hallazgos)} archivos relevantes en la categoría de personajes:\n")
    
    for archivo, claves in hallazgos:
        print(f"📁 Archivo: {archivo}")
        print(f"   🔑 Claves: {claves}")
        print("-" * 60)

if __name__ == "__main__":
    buscar_stats_exactas()