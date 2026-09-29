import json
import os


def inspeccionar_roles():
  # Apuntamos a la carpeta role dentro de BinData
  ruta_carpeta_role = "WutheringWaves_Data/BinData/role"

  print("=== INSPECCIONANDO LA CARPETA ROLE ===")

  if os.path.exists(ruta_carpeta_role):
    archivos_role = os.listdir(ruta_carpeta_role)
    print(
        f"Se encontraron {len(archivos_role)} archivos internos en la carpeta"
        " 'role':"
    )
    for arch in archivos_role:
      print(f" - {arch}")

    # Ubicamos específicamente el archivo roleinfo.json
    ruta_roleinfo = os.path.join(ruta_carpeta_role, "roleinfo.json")

    if os.path.exists(ruta_roleinfo):
      print("\n--- Leyendo estructura de roleinfo.json ---")
      with open(ruta_roleinfo, "r", encoding="utf-8") as f:
        datos = json.load(f)
        print(f"Tipo de estructura de datos: {type(datos)}")

        # Si es una lista, mostramos un resumen del primer personaje
        if isinstance(datos, list) and len(datos) > 0:
          print("Ejemplo del primer registro encontrado:")
          print(json.dumps(datos[0], indent=4, ensure_ascii=False)[:500])
        elif isinstance(datos, dict):
          primera_clave = list(datos.keys())[0]
          print(f"Claves principales detectadas. Ejemplo para '{primera_clave}':")
          print(
              json.dumps(datos[primera_clave], indent=4, ensure_ascii=False)[:500]
          )
    else:
      print("\nNo se encontró el archivo roleinfo.json en la ruta.")
  else:
    print("La carpeta role no existe.")


if __name__ == "__main__":
  inspeccionar_roles()