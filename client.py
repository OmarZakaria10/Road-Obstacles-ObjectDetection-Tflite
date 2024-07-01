import socket

def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8888))  # Adjust the IP address and port as needed
    
    try:
        while True:
            data = client_socket.recv(1024)  # Receive data from the server
            if not data:
                break
            print("Received data:", data.decode())
    except KeyboardInterrupt:
        print("Client stopped.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    tcp_client()
