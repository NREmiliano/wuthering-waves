import json
import os


def explorar_textmap_espanol():
    ruta_es = "WutheringWaves_Data/Textmaps/es"

    print("=== EXPLORANDO TEXTMAPS EN ESPAÑOL ===")

    if os.path.exists(ruta_es):
        archivos = os.listdir(ruta_es)
        print(f"Archivos en 'es': {archivos}")

        for archivo in archivos:
            if archivo.endswith(".json"):
                ruta_archivo = os.path.join(ruta_es, archivo)
                print(f"\nLeyendo archivo: {archivo}")

                with open(ruta_archivo, "r", encoding="utf-8") as f:
                    try:
                        datos = json.load(f)
                        print(f"Total de registros de texto: {len(datos)}")

                        # Buscamos si existe la llave relacionada con el personaje 1402
                        coincidencias = {
                            k: v
                            for k, v in datos.items()
                            if "1402" in str(k) or "1402" in str(v)
                        }
                        if coincidencias:
                            print(f"¡Encontrado para 1402!: {coincidencias}")
                        else:
                            print(
                                "No hay coincidencia exacta con 1402 en este archivo."
                            )

                    except Exception as e:
                        print(f"Error al leer el JSON: {e}")
                break
    else:
        print("No se encontró la carpeta 'es'.")


if __name__ == "__main__":
    explorar_textmap_espanol()