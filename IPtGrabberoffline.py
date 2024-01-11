import requests
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


def main():
    # Get the public IP address
    public_ip = get_public_ip()

    if public_ip:
        # Save the public IP address to a text file
        save_ip_to_file(public_ip, "public_ip.txt")
    else:
        print("Could not retrieve public IP.")

    # Get the local IP address
    local_ip = get_local_ip()

    if local_ip:
        # Save the local IP address to a text file
        save_ip_to_file(local_ip, "local_ip.txt")
    else:
        print("Could not retrieve local IP.")


if __name__ == "__main__":
    main()

