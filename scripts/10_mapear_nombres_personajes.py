import json
import os


def mapear_personajes():
    ruta_roleinfo = "WutheringWaves_Data/BinData/role/roleinfo.json"
    ruta_textmap_general = (
        "WutheringWaves_Data/Textmaps/es"  # O el archivo específico de texto
    )

    print("=== MAPEANDO IDS DE ROL CON NOMBRES ===")

    if os.path.exists(ruta_roleinfo):
        with open(ruta_roleinfo, "r", encoding="utf-8") as f:
            roles = json.load(f)

            print(f"Total de personajes en roleinfo: {len(roles)}\n")
            print(f"{'ID':<6} | {'NAME / NICKNAME':<30}")
            print("-" * 45)

            for rol in roles[:15]:  # Mostramos los primeros 15 personajes
                rid = rol.get("Id")
                rname = rol.get("Name")
                rnick = rol.get("NickName")
                print(f"{str(rid):<6} | {str(rname):<15} | {str(rnick)}")
    else:
        print("No se encontró el archivo roleinfo.json")


if __name__ == "__main__":
    mapear_personajes()