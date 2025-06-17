import subprocess

def crack_zip(archivo, diccionario):
    with open(diccionario, 'r') as f:
        for password in f:
            password = password.strip()
            result = subprocess.run(["unzip", "-P", password, archivo], capture_output=True)
            if result.returncode == 0:
                print(f"ContraseÃ±a encontrada: {password}")
                return
            else:
                print(f"ContraseÃ±a incorrecta: {password}")

# Ejemplo de uso:
archivo = input("Introduce la ruta del archivo: ")
diccionario = "/usr/share/wordlists/rockyou.txt"

crack_zip(archivo, diccionario)

