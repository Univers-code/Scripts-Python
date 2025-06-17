import requests

def check_extensions(ip):
    extensions = ["/administrator/", "/admin/", "/config/", "/private/", "/tmp/", "/data/",
                  "/includes/", "/cgi-bin/", "/api/", "/bin/", "/modules/", "/logs/", "/cache/"]

    for extension in extensions:
        url = f"http://{ip}{extension}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"La extensiÃ³n {extension} existe en {ip}")
            else:
                print(f"La extensiÃ³n {extension} no existe o no es accesible en {ip}")
        except requests.exceptions.RequestException as e:
            print(f"Error al verificar la extensiÃ³n {extension}: {e}")

if __name__ == "__main__":
    ip = input("IP: ")
    check_extensions(ip)

