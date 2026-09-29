import json
import os
import pandas as pd


def extraer_estadisticas_personajes():
    # Usamos la misma ruta estándar basada en la raíz del proyecto
    ruta_roleinfo = "WutheringWaves_Data/BinData/role/roleinfo.json"

    print("=== PROCESANDO ESTADÍSTICAS DE PERSONAJES ===")

    if os.path.exists(ruta_roleinfo):
        with open(ruta_roleinfo, "r", encoding="utf-8") as f:
            datos = json.load(f)

        lista_personajes = []

        # Iteramos sobre cada registro de personaje en el archivo JSON
        for personaje in datos:
            char_id = personaje.get("Id")
            nombre_ref = personaje.get("Name")
            rareza = personaje.get("QualityId")
            nivel_max = personaje.get("MaxLevel")
            tipo_arma = personaje.get("WeaponType")

            lista_personajes.append({
                "ID": char_id,
                "NombreRef": nombre_ref,
                "Rareza": rareza,
                "NivelMax": nivel_max,
                "TipoArma": tipo_arma,
            })

        # Convertimos los datos extraídos a un DataFrame de Pandas
        df_personajes = pd.DataFrame(lista_personajes)

        print(f"Se procesaron exitosamente {len(df_personajes)} personajes.")
        print("\n--- Vista previa de la tabla extraída ---")
        print(df_personajes.head())

        # Opcional: Guardarlo como un archivo CSV limpio en tu proyecto
        # df_personajes.to_csv("WutheringWaves_Data/personajes_resumen.csv", index=False)

    else:
        print("No se encontró el archivo roleinfo.json en la ruta especificada.")


if __name__ == "__main__":
    extraer_estadisticas_personajes()