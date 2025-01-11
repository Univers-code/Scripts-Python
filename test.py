import requests
from tqdm import tqdm
import time

# Enumeración de cabezeras

d = 0
while d < 1:
    esp = input("Especifique qué desea: Extraer datos de cabecera: C, Verificar certificado HTTPS: H, Verificar si es sensible a XSS o código malicioso: X, Extracción de datos para directorios: R: ")
    ip = input("Ingrese IP o URL: ")

    # Cabeceras
    def cab():
        for _ in tqdm(range(100), desc="Extrayendo:", unit='%', leave=False):
            time.sleep(0.05)
        response = requests.get(ip)
        for header, value in response.headers.items():
            print(f"{header}: {value}")

    # Verificar certificado HTTP SSL
    def val():
        for _ in tqdm(range(100), desc="Verificando: ", unit='%', leave=False):
            time.sleep(0.05)
        try:
            response = requests.get(ip, verify=True)
            print("Es true")
        except:
            print("False")

    # Verificar si es sensible a XSS o código malicioso
    def xxs():
        for _ in tqdm(range(100), desc="Verificando: ", unit='%', leave=False):
            time.sleep(0.05)
        params = {"search": "test", "id": "1"}
        response = requests.get(ip, params=params)
        print(response.text)

    # Extracción de datos robots.txt
    def rob():
        for _ in tqdm(range(100), desc="Extrayendo:", unit='%', leave=False):
            time.sleep(0.05)
        response = requests.get(f"{ip}/robots.txt")
        print(response.text)

    if esp == "C":
        cab()
    elif esp == "H":
        val()
    elif esp == "X":
        xxs()
    elif esp == "R":
        rob()
    else:
        print("Opción no válida.")

    cont = input("¿Deseas continuar o acabar? (1: Continuar, 2: Acabar): ")

    if cont == "2":
        d += 1  # Puedes incrementar d para salir del bucle
