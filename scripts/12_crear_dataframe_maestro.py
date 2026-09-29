import json
import os
import pandas as pd


def construir_diccionario_textmaps():
  ruta_es = (
      "../WutheringWaves_Data/Textmaps/es"
      if os.path.exists("../WutheringWaves_Data")
      else "WutheringWaves_Data/Textmaps/es"
  )
  textmaps_dict = {}

  if os.path.exists(ruta_es):
    for subcarpeta in os.listdir(ruta_es):
      ruta_sub = os.path.join(ruta_es, subcarpeta)
      if os.path.isdir(ruta_sub):
        for archivo_json in os.listdir(ruta_sub):
          if archivo_json.endswith(".json"):
            try:
              with open(
                  os.path.join(ruta_sub, archivo_json), "r", encoding="utf-8"
              ) as f:
                datos = json.load(f)
                if isinstance(datos, list):
                  for item in datos:
                    if isinstance(item, dict):
                      rid = item.get("Id")
                      content = item.get("Content")
                      if rid:
                        textmaps_dict[str(rid)] = content
            except Exception:
              pass
  return textmaps_dict


def generar_dataframe_personajes():
  ruta_roleinfo = (
      "../WutheringWaves_Data/BinData/role/roleinfo.json"
      if os.path.exists("../WutheringWaves_Data")
      else "WutheringWaves_Data/BinData/role/roleinfo.json"
  )

  print("=== CONSTRUYENDO DATAFRAME MAESTRO DE PERSONAJES ===")

  textmaps = construir_diccionario_textmaps()

  if os.path.exists(ruta_roleinfo):
    with open(ruta_roleinfo, "r", encoding="utf-8") as f:
      roles = json.load(f)

      lista_datos = []
      for rol in roles:
        rid = rol.get("Id")
        clave_nombre = rol.get("Name")
        nombre_traducido = textmaps.get(str(clave_nombre), "Desconocido")

        lista_datos.append({
            "Character_ID": rid,
            "Text_Key": clave_nombre,
            "Character_Name": nombre_traducido,
        })

      # Creamos el DataFrame con Pandas
      df_personajes = pd.DataFrame(lista_datos)

      # Limpieza básica: filtramos o ordenamos si es necesario
      print(f"\nDataFrame creado con éxito. Total de filas: {len(df_personajes)}")
      print("\nPrimeras 5 filas del DataFrame:")
      print(df_personajes.head())

      # Exportamos a CSV para futuras consultas en el pipeline de datos
      output_dir = "../WutheringWaves_Data/processed" if os.path.exists("../WutheringWaves_Data") else "WutheringWaves_Data/processed"
      os.makedirs(output_dir, exist_ok=True)
      output_path = os.path.join(output_dir, "personajes_mapeados.csv")
      
      df_personajes.to_csv(output_path, index=False, encoding="utf-8")
      print(f"\n¡DataFrame exportado exitosamente a: {output_path}!")

      return df_personajes
  else:
      print(f"No se encontró roleinfo.json en la ruta: {ruta_roleinfo}")


if __name__ == "__main__":
  df = generar_dataframe_personajes()