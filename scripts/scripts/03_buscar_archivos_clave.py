import os


def buscar_archivos_clave():
  # Ruta de la carpeta BinData dentro de los datos descargados
  ruta_bindata = "WutheringWaves_Data/BinData"

  # Palabras clave orientadas a buscar datos de personajes, equipo y avatares
  palabras_clave = ["role", "character", "weapon", "card", "avatar"]

  print("=== BUSCANDO ARCHIVOS CLAVE EN BINDATA ===")

  if os.path.exists(ruta_bindata):
    archivos = os.listdir(ruta_bindata)
    print(f"Total de archivos analizados en BinData: {len(archivos)}")

    print("\n--- Coincidencias encontradas ---")
    encontrados = 0
    for archivo in archivos:
      # Verificamos si alguna palabra clave está contenida en el nombre del archivo
      if any(palabra in archivo.lower() for palabra in palabras_clave):
        print(f" - {archivo}")
        encontrados += 1

    print(f"\nSe encontraron {encontrados} archivos relevantes.")
  else:
    print("La carpeta BinData no se encuentra en la ruta especificada.")


if __name__ == "__main__":
  buscar_archivos_clave()