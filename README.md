Obtener, Guardar y Enviar IP Pública por Email
Este script de Python utiliza el servicio web httpbin.org para obtener la dirección IP pública de la máquina en la que se ejecuta. La dirección IP pública se recupera mediante una solicitud HTTP al endpoint /ip de httpbin.org. Luego, la dirección IP se guarda en un archivo de texto local llamado public_ip.txt y se envía por correo electrónico.

Uso
Ejecuta el script Python get_public_ip.py.
La dirección IP pública se obtendrá desde httpbin.org.
La dirección IP se guardará en el archivo public_ip.txt.
La dirección IP también se enviará por correo electrónico.
Requisitos
Asegúrate de tener el módulo requests instalado antes de ejecutar el script. Puedes instalarlo ejecutando pip install requests.

Nota: Este script requiere acceso a Internet para obtener la dirección IP pública y enviar el correo electrónico.

Configuración del Correo Electrónico
Asegúrate de configurar correctamente las variables sender_email, receiver_email, y password en el código para permitir el envío del correo electrónico.



