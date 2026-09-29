import json
import os


def construir_diccionario_textmaps():
    ruta_es = "WutheringWaves_Data/Textmaps/es"
    textmaps_dict = {}

    # Cargamos todos los textos localizados en un solo diccionario global para búsqueda rápida
    if os.path.exists(ruta_es):
        for subcarpeta in os.listdir(ruta_es):
            ruta_sub = os.path.join(ruta_es, subcarpeta)
            if os.path.isdir(ruta_sub):
                for archivo_json in os.listdir(ruta_sub):
                    if archivo_json.endswith(".json"):
                        try:
                            with open(
                                os.path.join(ruta_sub, archivo_json),
                                "r",
                                encoding="utf-8",
                            ) as f:
                                datos = json.load(f)
                                if isinstance(datos, list):
                                    for item in datos:
                                        if isinstance(item, dict):
                                            rid = item.get("Id")
                                            content = item.get("Content")
                                            if rid:
                                                textmaps_dict[str(rid)] = (
                                                    content
                                                )
                        except Exception:
                            pass
    return textmaps_dict


def mapear_calculadora_daño():
    ruta_roleinfo = "WutheringWaves_Data/BinData/role/roleinfo.json"
    print("=== GENERANDO MAESTRO DE PERSONAJES PARA CALCULADORA ===")

    textmaps = construir_diccionario_textmaps()
    print(
        f"Textmaps cargados en memoria: {len(textmaps)} referencias de texto.\n"
    )

    if os.path.exists(ruta_roleinfo):
        with open(ruta_roleinfo, "r", encoding="utf-8") as f:
            roles = json.load(f)

            print(
                f"{'ID':<6} | {'CLAVE DE TEXTO':<25} | {'NOMBRE TRADUCIDO'}"
            )
            print("-" * 65)

            for rol in roles:
                rid = rol.get("Id")
                clave_nombre = rol.get("Name")  # Ej: RoleInfo_1402_Name

                # Buscamos la clave en nuestro diccionario de textmaps
                nombre_traducido = textmaps.get(
                    str(clave_nombre), "[No encontrado en Textmaps]"
                )

                # Si encontramos el nombre (o al menos imprimimos los principales)
                if nombre_traducido:
                    print(
                        f"{str(rid):<6} | {str(clave_nombre):<25} | {nombre_traducido}"
                    )
    else:
        print("No se encontró roleinfo.json")


if __name__ == "__main__":
    mapear_calculadora_daño()