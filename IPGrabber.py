import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket


def get_public_ip():
    """
    Gets the public IP address of the device using httpbin.org.
    """
    try:
        response = requests.get("https://httpbin.org/ip")
        ip_data = response.json()
        public_ip = ip_data.get("origin")
        return public_ip
    except Exception as e:
        print(f"Error fetching public IP: {e}")
        return None


def get_local_ip():
    """
    Gets the local IP address of the device.
    """
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
        return local_ip
    except Exception as e:
        print(f"Error fetching local IP: {e}")
        return None


def save_ip_to_file(ip, filename):
    """
    Saves the IP address to a text file.
    """
    try:
        with open(filename, "w") as file:
            file.write(ip)
        print(f"IP ({ip}) has been saved to {filename}")
    except Exception as e:
        print(f"Error saving IP: {e}")


def send_email(subject, body):
    """
    Sends an email with the IP addresses.
    """
    try:
        sender_email = "your_email@gmail.com"  # Your email address
        receiver_email = "receiver_email@gmail.com"  # Recipient's email address
        password = "your_password"  # Your email password

        # Configure the message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        print("Email sent successfully.")

    except Exception as e:
        print(f"Error sending email: {e}")


def main():
    # Get the public IP address
    public_ip = get_public_ip()

    if public_ip:
        # Save the public IP address to a text file
        save_ip_to_file(public_ip, "public_ip.txt")

        # Send the public IP address via email
        subject = "Public IP Address"
        body = f"The current public IP address is: {public_ip}"
        send_email(subject, body)
    else:
        print("Could not retrieve public IP.")

    # Get the local IP address
    local_ip = get_local_ip()

    if local_ip:
        # Save the local IP address to a text file
        save_ip_to_file(local_ip, "local_ip.txt")

        # Send the local IP address via email
        subject = "Local IP Address"
        body = f"The current local IP address is: {local_ip}"
        send_email(subject, body)
    else:
        print("Could not retrieve local IP.")


if __name__ == "__main__":
    main()

