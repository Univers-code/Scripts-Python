# Esto solo funciona en paginas webs, para hacer peticiones

import requests
import os

#URL or ip
ip = input("Ingresar ip")

# Names or list
name = input("Lista de nombres o nombre")

passd = input("List os password or password")

#passwords


#Iterar sobre cada contrasena mandando un post a la pagina
for dete in passd:
    data = {"username": name, "password": passd}
    response = requests.post(ip,data=data)
    if "Invalid password" not in response.text:
        print(f"Password found: {passd}")
        break