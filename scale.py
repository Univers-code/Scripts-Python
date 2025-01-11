# Encontrar carpetas para escalar privilegios con find y sudo -l
# Implementar codigo que verifique cada uno de los archivos de un posible SUID
# MEdiante requests mandar solicitud a gtfgobis para verificar cada uno y obtener el codigo para escalar

# Scripts para escalar privilegios de forma automatizada

import os
import subprocess
import stat  # Asegúrate de importar el módulo 'stat'

# Limitar el alcance de la búsqueda
search_dirs = ["/usr", "/bin", "/sbin"]
scan = subprocess.run(["find"] + search_dirs + ["-xdev", "-perm", "-4000"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)

# Procesar la salida del comando
res = scan.stdout.strip().split('\n')

# Títulos para una mejor visualización
print(f"{'Archivo':<60} {'UID':<10} {'GID':<10}")

for suid in res:
    if suid:  # Comprobar si hay una ruta válida
        try:
            file2 = os.stat(suid)
            if file2.st_mode & stat.S_ISUID:
                # Extraer información relevante
                uid = file2.st_uid
                gid = file2.st_gid
                # Imprimir de forma sintetizada
                print(f"{suid:<60} {uid:<10} {gid:<10}")
        except FileNotFoundError:
            print(f"No se encuentra archivo SUID: {suid}")
        except PermissionError:
            print(f"No tiene permiso para acceder a {suid}")

        







