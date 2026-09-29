import os
import json

def buscar_e_inspeccionar():
    print("=== BUSCANDO E INSPECCIONANDO ROLEPROPERTYGROWTH.JSON ===")
    
    # Buscamos el archivo en todo el directorio de trabajo
    ruta_encontrada = None
    for root, dirs, files in os.walk("."):
        if "rolepropertygrowth.json" in files:
            ruta_encontrada = os.path.join(root, "rolepropertygrowth.json")
            break
            
    if not ruta_encontrada and os.path.exists("../WutheringWaves_Data"):
        for root, dirs, files in os.walk("../WutheringWaves_Data"):
            if "rolepropertygrowth.json" in files:
                ruta_encontrada = os.path.join(root, "rolepropertygrowth.json")
                break

    if ruta_encontrada:
        print(f"¡Archivo encontrado en: {ruta_encontrada}!\n")
        with open(ruta_encontrada, 'r', encoding='utf-8') as f:
            datos = json.load(f)
            if isinstance(datos, list) and len(datos) > 0:
                print(f"Total de registros de crecimiento: {len(datos)}\n")
                print("Muestra de los primeros 5 registros:")
                for item in datos[:5]:
                    print(item)
    else:
        print("No se pudo localizar rolepropertygrowth.json en ninguna subcarpeta. Verifica si la carpeta de datos está descomprimida.")

if __name__ == "__main__":
    buscar_e_inspeccionar()