import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_public_ip():
    """
    Obtiene la dirección IP pública del equipo utilizando httpbin.org.
    """
    try:
        response = requests.get('https://httpbin.org/ip')
        ip_data = response.json()
        public_ip = ip_data.get('origin')
        return public_ip
    except Exception as e:
        print(f"Error al obtener la IP pública: {e}")
        return None

def save_ip_to_file(ip):
    """
    Guarda la dirección IP pública en un archivo de texto.
    """
    try:
        with open("public_ip.txt", "w") as file:
            file.write(ip)
        print(f"La IP pública ({ip}) se ha guardado en public_ip.txt")
    except Exception as e:
        print(f"Error al guardar la IP pública: {e}")

def send_email(subject, body):
    """
    Envía un correo electrónico con la dirección IP pública.
    """
    try:
        sender_email = 'tucorreo@gmail.com'  # Tu dirección de correo electrónico
        receiver_email = 'destinatario@gmail.com'  # La dirección de correo electrónico del destinatario
        password = 'tucontraseña'  # Tu contraseña de correo electrónico

        # Configura el mensaje
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Conéctate al servidor SMTP y envía el correo electrónico
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            
        print("Correo electrónico enviado correctamente.")
        
    except Exception as e:
        print(f"Error al enviar el correo electrónico: {e}")

def main():
    # Obtiene la dirección IP pública
    public_ip = get_public_ip()

    if public_ip:
        # Guarda la dirección IP pública en un archivo de texto
        save_ip_to_file(public_ip)

        # Envía la dirección IP pública por correo electrónico
        subject = 'Dirección IP Pública'
        body = f"La dirección IP pública actual es: {public_ip}"
        send_email(subject, body)
    else:
        print("No se pudo obtener la IP pública.")

if __name__ == "__main__":
    main()
