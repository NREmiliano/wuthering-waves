import json
import os


def explorar_textmaps():
    # Buscamos en la carpeta Textmaps del proyecto
    ruta_textmaps = "WutheringWaves_Data/Textmaps"

    print("=== EXPLORANDO CARPETA DE TEXTMAPS ===")

    if os.path.exists(ruta_textmaps):
        archivos = os.listdir(ruta_textmaps)
        print(f"Archivos encontrados en Textmaps: {archivos}")

        # Buscamos un archivo json típico de textmaps (ej. client.json o similar)
        for archivo in archivos:
            if archivo.endswith(".json"):
                ruta_archivo = os.path.join(ruta_textmaps, archivo)
                print(f"\nInspeccionando archivo: {archivo}")

                with open(ruta_archivo, "r", encoding="utf-8") as f:
                    try:
                        # Cargamos una muestra o el contenido completo si no es muy pesado
                        datos = json.load(f)
                        if isinstance(datos, dict):
                            print(
                                f"  - Es un diccionario con {len(datos)} entradas."
                            )
                            # Mostramos un par de ejemplo de llaves que contengan '1402'
                            ejemplos = {
                                k: v
                                for k, v in list(datos.items())[:5]
                                if "1402" in str(k) or "1402" in str(v)
                            }
                            if ejemplos:
                                print(f"  - Ejemplos con 1402: {ejemplos}")
                            else:
                                # Mostramos las primeras 3 llaves y valores genéricos
                                primeras_llaves = list(datos.items())[:3]
                                print(f"  - Primeras entradas: {primeras_llaves}")
                        elif isinstance(datos, list):
                            print(
                                f"  - Es una lista con {len(datos)} elementos."
                            )
                    except Exception as e:
                        print(f"  - No se pudo leer como JSON estándar: {e}")
                break  # Analizamos el primero para empezar
    else:
        print("No se encontró la carpeta Textmaps.")


if __name__ == "__main__":
    explorar_textmaps()
