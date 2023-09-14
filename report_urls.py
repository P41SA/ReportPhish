import requests

# URL de la página de informe de phishing de Google Safe Browsing
report_url = "https://safebrowsing.google.com/safebrowsing/report_phish/"

# Función para enviar un informe de phishing para una URL dada
def report_phishing(url):
    try:
        # Realiza una solicitud POST a la página de informe de phishing
        response = requests.post(report_url, data={"url": url})

        # Comprueba si la solicitud fue exitosa (código de respuesta 200)
        if response.status_code == 200:
            print(f"Se ha enviado un informe de phishing para la URL: {url}")
        else:
            print(f"No se pudo enviar un informe de phishing para la URL: {url}")

    except Exception as e:
        print(f"Error al enviar un informe de phishing para la URL {url}: {str(e)}")

# Leer las URLs desde el archivo urls.txt
with open("urls.txt", "r") as file:
    urls = file.read().splitlines()

# Itera a través de la lista de URLs y envía informes de phishing para cada una
for url in urls:
    report_phishing(url)

