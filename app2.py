# Importar librerias a usar 
from tqdm import tqdm
import subprocess as d
import time
import os

print("-----------")
print("|Scan NMAP|")
print("-----------")

# Ip a escanear
ip = input("Ingrese la IP: ")

# limpiar la consola
os.system("clear")


print("Este proceso puede tomar un tiempo..")
print("Iniciando escaneo con nmap...")

# Barra de progreso del escaneo
for _ in tqdm(range(100), desc="Escaneando con Nmap", unit='%', leave=False):
    time.sleep(0.05)  

# Ejecutar el escaneo
result = d.run(["sudo", "nmap", "-p-", "--open", "-sS", "-sV", "-sC", "-Pn", ip, "-oN", "scan.txt"],
               text=True, check=True, capture_output=True)

# Mostrar mensaje final después de que se complete el escaneo
print("Escaneo completado. Se ha guardado exitosamente en scan.txt.")