# Web Scanner #

### Descripción
**Web Scanner** es una herramienta desarrollada en Python para realizar pruebas de seguridad en servidores web, esta herramienta permite evaluar configuraciones de seguridad mediante el análisis de cabeceras HTTP, métodos inseguros, versiones de SSL/TLS, información del servidor, y listados de directorios, además, incluye la opción de usar un proxy para realizar las solicitudes desde una IP diferente, preservando la privacidad del usuario.

### Disclaimer
Esta herramienta fue creada por Técnicos en Hacking exclusivamente para fines educativos y pruebas en entornos controlados, **No nos hacemos responsables del mal uso de esta herramienta**, usala únicamente en sistemas que posea o con el debido permiso.

### Características:
- **Análisis de cabeceras de seguridad**: Verifica la presencia de cabeceras recomendadas para seguridad como `Content-Security-Policy`, `X-Frame-Options`, entre otras.
- **Verificación de métodos HTTP inseguros**: Detecta métodos inseguros como `OPTIONS`, `TRACE`, `PUT`, y `DELETE`.
- **Detección de versiones SSL/TLS**: Comprueba las versiones de SSL/TLS soportadas por el servidor.
- **Información del servidor**: Extrae información básica del servidor a partir de la cabecera `Server`.
- **Detección de listado de directorios**: Evalúa si el servidor tiene habilitado el listado de directorios.
- **Soporte de proxy**: Permite realizar solicitudes a través de un proxy, ocultando la IP del usuario.

### Instalación:

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/TecnicosEnHacking/WebScanner
   cd web-vulnerability-scanner
   ```
2. Instalar dependencias
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecucion de la herramienta
   ```bash
   python WebScanner.py
   ```
