import socket
import argparse
import logging

def escanear_puertos(ip, rango_puertos):
    puertos_abiertos = []

    for puerto in range(rango_puertos[0], rango_puertos[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1) 
        try:
            resultado = sock.connect_ex((ip, puerto))
            if resultado == 0:
                logging.info(f"Puerto {puerto} abierto")
                puertos_abiertos.append(puerto)
        except Exception as e:
            logging.error(f"Error al escanear puerto {puerto}: {str(e)}")
        finally:
            sock.close()

    return puertos_abiertos

def main():
    parser = argparse.ArgumentParser(description="Escaneo de puertos en una dirección IP")
    parser.add_argument("ip", help="Dirección IP a escanear")
    parser.add_argument("inicio", type=int, help="Puerto de inicio del rango")
    parser.add_argument("fin", type=int, help="Puerto de fin del rango")
    
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        rango_puertos = (args.inicio, args.fin)
        puertos_abiertos = escanear_puertos(args.ip, rango_puertos)
        logging.info("\nPuertos abiertos: %s", puertos_abiertos)
    except Exception as e:
        logging.error(f"Error durante el escaneo: {str(e)}")

if __name__ == "__main__":
    main()
