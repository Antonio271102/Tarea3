#!/usr/bin/python3
import nmap
import os

def run_nmap(hosts, ports, arguments, sudo=False):
    nm = nmap.PortScanner()
    
    # Configurar opciones de sudo si es necesario
    sudo_cmd = 'sudo ' if sudo else ''
    
    # Construir el comando nmap
    cmd = f'{sudo_cmd}nmap {arguments} -p {ports} {hosts}'
    
    # Ejecutar el comando
    os.system(cmd)

def main():
    print("Bienvenido al escáner Nmap.")
    hosts = input("Ingrese el rango de hosts a escanear (p.ej. 192.168.1.1-100): ")
    ports = input("Ingrese los puertos a escanear (p.ej. 1-1000): ")
    arguments = input("Ingrese argumentos adicionales de Nmap (p.ej. -sV -A): ")
    use_sudo = input("¿Desea ejecutar el comando como superusuario? (s/n): ").lower() == 's'
    
    # Ejecutar el escaneo
    run_nmap(hosts, ports, arguments, use_sudo)

if __name__ == "__main__":
    main()
