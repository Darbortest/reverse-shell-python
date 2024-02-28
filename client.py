import requests



ipaddr = '10.9.3.102'  # Replace with the actual server IP address

port = 4201               # Replace with the actual server port



def send_command(command):

    url = f'http://{ipaddr}:{port}/commander/run?command={command}'

    response = requests.get(url)

    print(response.text)



while True:

    user_input = input("Enter command (type 'exit' to quit): ")

    if user_input.lower() == 'exit':

        break



    send_command(user_input)

