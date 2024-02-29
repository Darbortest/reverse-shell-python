import requests
import subprocess

server_url = "http://10.9.3.102:4200"  # Zmie? na odpowiedni adres i port serwera

while True:
    command = input("Ready to enter the website (type 'exit' to quit): ")
    if command.lower() == 'exit':
        break

    url = f"{server_url}/run-command?command={command}"
    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: {response.status_code}")

