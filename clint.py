import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8888))  # Connect to port 8888 on localhost
    print("Connected to the server.")
    
    while True:
        message = input("You: ")
        client.send(message.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(f"Server: {response}")

if __name__ == "__main__":
    main()
