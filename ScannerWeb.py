import requests

def escanear_vulnerabilidades(url):
    encabezados_sospechosos = ["Server", "X-Powered-By", "X-AspNet-Version"]

    try:
        respuesta = requests.get(url)

        print(f"\nInformación de la respuesta para {url}:")
        print(f"Estado de la respuesta: {respuesta.status_code}")
        print("Encabezados de la respuesta:")
        for encabezado, valor in respuesta.headers.items():
            print(f"{encabezado}: {valor}")

        print("\nPosibles vulnerabilidades:")
        for encabezado in encabezados_sospechosos:
            if encabezado in respuesta.headers:
                print(f"¡Posible vulnerabilidad! Encabezado {encabezado} encontrado.")

    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {str(e)}")

if __name__ == "__main__":
    url_objetivo = "https://tecnica1merlo.edu.ar/"  #url 
    escanear_vulnerabilidades(url_objetivo)
