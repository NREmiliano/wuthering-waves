import json
import os


def analizar_campos_roleinfo():
    ruta_roleinfo = "WutheringWaves_Data/BinData/role/roleinfo.json"
    print("=== ANALIZANDO CAMPOS DE TEXTO Y NOMBRES EN ROLEINFO ===")

    if os.path.exists(ruta_roleinfo):
        with open(ruta_roleinfo, "r", encoding="utf-8") as f:
            datos = json.load(f)

            if isinstance(datos, list) and len(datos) > 0:
                print(f"Total de registros en roleinfo.json: {len(datos)}\n")

                # Mostramos los campos clave del primer registro para entender la estructura
                primer_registro = datos[0]
                print("--- Campos disponibles en un registro ---")
                for k in primer_registro.keys():
                    print(f" • {k}")

                print(
                    "\n--- Muestra de campos relevantes (ID, Nombres, Rutas) ---"
                )
                for i, entry in enumerate(
                    datos[:3]
                ):  # Revisamos los primeros 3 personajes
                    print(f"\nPersonaje #{i + 1}:")
                    for k, v in entry.items():
                        if any(
                            term in k.lower()
                            for term in [
                                "id",
                                "name",
                                "text",
                                "desc",
                                "title",
                                "portrait",
                            ]
                        ):
                            print(f"   {k} : {v}")
    else:
        print(f"No se encontró el archivo en: {ruta_roleinfo}")


if __name__ == "__main__":
    analizar_campos_roleinfo()