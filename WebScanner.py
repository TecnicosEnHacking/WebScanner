import requests
import ssl
import socket
import re
from requests.exceptions import RequestException

security_headers = [
    'Content-Security-Policy',
    'X-Content-Type-Options',
    'X-Frame-Options',
    'Strict-Transport-Security',
    'X-XSS-Protection'
]

insecure_methods = ['OPTIONS', 'TRACE', 'PUT', 'DELETE']

user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"

def disclaimer():
    print("\n*******************")
    print("   Herramienta creada por Técnicos en Hacking")
    print("   No nos hacemos responsables del mal uso de esta herramienta")
    print("   Utilícela solo en entornos controlados y con permiso.")
    print("*******************\n")

def check_headers(url, proxies=None):
    print("\n[+] Comprobando cabeceras de seguridad...")
    headers_report = {}
    try:
        response = requests.get(url, headers={'User-Agent': user_agent}, proxies=proxies, timeout=10)
        for header in security_headers:
            headers_report[header] = "Presente" if header in response.headers else "Faltante"
        
        for header, status in headers_report.items():
            print(f"{header}: {status}")
    except RequestException as e:
        print(f"Error al verificar cabeceras de seguridad: {e}")

def check_http_methods(url, proxies=None):
    print("\n[+] Verificando métodos HTTP permitidos...")
    methods_report = {}
    for method in insecure_methods:
        try:
            response = requests.request(method, url, headers={'User-Agent': user_agent}, proxies=proxies, timeout=10)
            if response.status_code < 400:
                methods_report[method] = "Permitido"
            else:
                methods_report[method] = "No permitido"
        except RequestException:
            methods_report[method] = "Error en la solicitud"
    
    for method, status in methods_report.items():
        print(f"{method}: {status}")

def check_ssl_tls(url):
    print("\n[+] Verificando versiones de SSL/TLS...")
    ssl_report = {}
    hostname = url.replace("https://", "").replace("http://", "").split("/")[0]
    versions = {
        ssl.PROTOCOL_TLSv1: "TLSv1",
        ssl.PROTOCOL_TLSv1_1: "TLSv1.1",
        ssl.PROTOCOL_TLSv1_2: "TLSv1.2",
        ssl.PROTOCOL_TLS_CLIENT: "TLSv1.3"
    }

    for protocol, name in versions.items():
        context = ssl.SSLContext(protocol)
        try:
            with socket.create_connection((hostname, 443), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    ssl_report[name] = "Soportado"
        except ssl.SSLError:
            ssl_report[name] = "No soportado"
        except Exception as e:
            ssl_report[name] = f"Error: {e}"
    
    for version, status in ssl_report.items():
        print(f"{version}: {status}")

def check_server_info(url, proxies=None):
    print("\n[+] Obteniendo información del servidor...")
    try:
        response = requests.get(url, headers={'User-Agent': user_agent}, proxies=proxies, timeout=10)
        server_info = response.headers.get("Server", "No especificado")
        print(f"Servidor: {server_info}")
    except RequestException as e:
        print(f"Error al obtener información del servidor: {e}")

def check_directory_listing(url, proxies=None):
    print("\n[+] Comprobando listado de directorios...")
    try:
        response = requests.get(url, headers={'User-Agent': user_agent}, proxies=proxies, timeout=10)
        if re.search(r"Index of|Directory listing", response.text, re.I):
            print("¡Advertencia! Listado de directorios habilitado.")
        else:
            print("Listado de directorios deshabilitado.")
    except RequestException as e:
        print(f"Error al comprobar listado de directorios: {e}")

def main():
    disclaimer()
    print("Scanner de Vulnerabilidades para Servidores Web - Técnicos en Hacking")
    
    url = input("Ingrese la URL del servidor (e.g., https://example.com): ")
    
    use_proxy = input("¿Quieres utilizar un proxy para ocultar tu IP? (s/n): ").strip().lower()
    proxies = None
    if use_proxy == 's':
        proxy_ip = input("Ingrese la IP del proxy: ")
        proxy_port = input("Ingrese el puerto del proxy: ")
        proxies = {
            "http": f"http://{proxy_ip}:{proxy_port}",
            "https": f"http://{proxy_ip}:{proxy_port}"
        }
        print(f"Usando proxy {proxy_ip}:{proxy_port} para la solicitud...")

    check_headers(url, proxies)
    check_http_methods(url, proxies)
    check_ssl_tls(url)
    check_server_info(url, proxies)
    check_directory_listing(url, proxies)

    try:
        ip_check_url = "https://api.ipify.org"  # Servicio para verificar la IP de salida
        ip_response = requests.get(ip_check_url, proxies=proxies, timeout=10)
        print(f"\nLa solicitud se realizó desde la siguiente IP: {ip_response.text}")
    except RequestException as e:
        print("Error al verificar la IP de salida:", e)

    print("\n[+] Escaneo completado. Recuerde realizar estas pruebas en entornos controlados.")

if __name__ == "__main__":
    main()
