import socket

HOST = '127.0.0.1'
PORT = 8080

def handle_request(client_socket):
    with open('index.html', 'r') as file:
        content = file.read()

    response = f'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{content}'
    client_socket.sendall(response.encode('utf-8'))

def run_web_server():
    try:
        # Create a socket and bind it to the specified address and port
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print(f"Web server listening on http://{HOST}:{PORT}/")

        while True:
            # Wait for incoming connections
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            # Handle the client's request
            handle_request(client_socket)

            # Close the connection
            client_socket.close()

    except KeyboardInterrupt:
        print("\nWeb server stopped.")

    finally:
        server_socket.close()

if __name__ == "__main__":
    run_web_server()
