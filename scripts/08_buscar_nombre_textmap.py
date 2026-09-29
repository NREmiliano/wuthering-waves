import json
import os


def inspeccionar_roleinfo_personaje():
    # Ajusta la ruta según donde tengas ubicado tu roleinfo.json
    ruta_roleinfo = "WutheringWaves_Data/BinData/role/roleinfo.json"
    
    print("=== INSPECCIONANDO DATOS DEL PERSONAJE 1402 EN ROLEINFO ===")

    if os.path.exists(ruta_roleinfo):
        with open(ruta_roleinfo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            
            # Buscamos el registro que coincida con el ID 1402 (puede estar como 'Id' o llave numérica)
            encontrado = False
            for entry in datos:
                # Verificamos diferentes posibles nombres de la llave del ID
                id_actual = entry.get("Id") or entry.get("id") or entry.get("ID")
                
                if str(id_actual) == "1402":
                    encontrado = True
                    print(f"\n[¡REGISTRO ENCONTRADO EN ROLEINFO!]")
                    for k, v in entry.items():
                        print(f"   {k} : {v}")
                    break
            
            if not encontrado:
                print("No se encontró el ID 1402 directamente en roleinfo.json.")
    else:
        print(f"No se encontró el archivo en: {ruta_roleinfo}")


if __name__ == "__main__":
    inspeccionar_roleinfo_personaje()