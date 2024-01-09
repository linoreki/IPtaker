# IP Public Taker

A Python script that retrieves the public IP address of the machine, saves it to a text file, and sends it via email.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The IP Public Taker is a simple Python script that leverages the httpbin.org service to obtain the public IP address of the machine it runs on. It saves this information to a local text file named `public_ip.txt` and optionally sends it via email.

## Features

- Obtains the public IP address using httpbin.org.
- Saves the public IP address to a local text file.
- Optionally sends the public IP address via email.

## Requirements

- Python 3.11
- `requests` module (install using `pip install requests`)

## Usage

1. Run the Python script `get_public_ip.py`.
2. The public IP address is obtained from httpbin.org.
3. The public IP is saved in the file `public_ip.txt`.
4. Optionally, the public IP is sent via email.

```bash
# Example command
$ python get_public_ip.py
