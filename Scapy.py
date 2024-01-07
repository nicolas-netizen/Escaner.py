import scapy.all as scapy

def mostrar_interfaces():
    interfaces = scapy.get_if_list()
    print("Interfaces de red disponibles:")
    for interface in interfaces:
        print(f"Nombre: {interface} - Descripción: {scapy.get_if_raw_hwaddr(interface)}")

mostrar_interfaces()
