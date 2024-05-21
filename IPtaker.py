#!/usr/bin/env python3
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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


def save_ip_to_file(ip):
    """
    Saves the public IP address to a text file.
    """
    try:
        with open("public_ip.txt", "w") as file:
            file.write(ip)
        print(f"Public IP ({ip}) has been saved to public_ip.txt")
    except Exception as e:
        print(f"Error saving public IP: {e}")


def send_email(subject, body):
    """
    Sends an email with the public IP address.
    """
    try:
        sender_email = "your_email@gmail.com"  # Your email address
        receiver_email = "recipient@gmail.com"  # Recipient's email address
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
        save_ip_to_file(public_ip)

        # Send the public IP address via email
        subject = "Public IP Address"
        body = f"The current public IP address is: {public_ip}"
        send_email(subject, body)
    else:
        print("Could not retrieve public IP.")


if __name__ == "__main__":
    main()
