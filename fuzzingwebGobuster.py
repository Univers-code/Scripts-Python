import subprocess as d
import time
import os

try:
  # URL or IP input
  ip = input("IP o URL: ")


  library = input("Predeterminada: P , Propia: M: ")
  custom_library = ""

  if library == "P":
   
    library = "/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt"

   
    fuzz = d.run(["gobuster", "dir", "-u", ip, "-w", library, "-x", "php,py,js,conf,log,html,css,xml,txt", "-t", "64"], text=True, check=True, capture_output=True)
  else:
  
    custom_library = input("Introduce la ruta a tu diccionario: ")
    library = custom_library

  
    fuzz = d.run(["gobuster", "dir", "-u", ip, "-w", library, "-x", "php,py,js,conf,log,html,css,xml,txt", "-t", "64"], text=True, check=True, capture_output=True)


except Exception as e:
  print(f"An error occurred: {e}")


  if library == custom_library and not os.path.exists(custom_library):
    print(f"Error: Custom library file not found: {custom_library}")