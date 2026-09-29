import os


def explorar_raiz():
  # Definimos la ruta de la carpeta de datos descargada
  ruta_datos = "WutheringWaves_Data"

  print("=== CONTENIDO PRINCIPAL DEL REPOSITORIO DE WUWAGAME ===")

  # Verificamos si la carpeta realmente existe en nuestra computadora
  if os.path.exists(ruta_datos):
    # Listamos todos los elementos (archivos y subcarpetas) que contiene
    for item in os.listdir(ruta_datos):
      print(f" - {item}")
  else:
    print("La ruta de datos no existe. Asegúrate de haber clonado el repositorio.")


if __name__ == "__main__":
  explorar_raiz()