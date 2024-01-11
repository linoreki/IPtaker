import requests


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


def main():
    # Gets the public IP address
    public_ip = get_public_ip()

    if public_ip:
        # Saves the public IP address to a text file
        save_ip_to_file(public_ip)
    else:
        print("Could not retrieve public IP.")


if __name__ == "__main__":
    main()
