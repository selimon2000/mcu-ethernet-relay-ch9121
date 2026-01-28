import socket
import threading
import time

class TCPBridgeServer:
    def __init__(self, host='192.168.1.100', port=1000):
        self.host = host
        self.port = port
        self.socket = None
        self.client_socket = None
        self.client_address = None
        self.is_running = False
        
    def start_server(self):
        """Start the TCP server and listen for connections"""
        try:
            # Create TCP socket
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Allow reuse of address
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # Bind to the specified host and port
            self.socket.bind((self.host, self.port))
            # Listen for incoming connectionsL0-OFF
            self.socket.listen(1)
            
            print(f"TCP Server started on {self.host}:{self.port}")
            print("Waiting for 2-CH UART TO ETH module to connect...")
            
            self.is_running = True
            
            # Accept client connection
            self.client_socket, self.client_address = self.socket.accept()
            print(f"Connected to client: {self.client_address}")
            
            # Start threads for sending and receiving
            receive_thread = threading.Thread(target=self.receive_data)
            send_thread = threading.Thread(target=self.send_data)
            
            receive_thread.daemon = True
            send_thread.daemon = True
            
            receive_thread.start()
            send_thread.start()
            
            # Keep main thread alive
            while self.is_running:
                time.sleep(1)
                
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.stop_server()
    
    def receive_data(self):
        """Receive data from the 2-CH module"""
        while self.is_running and self.client_socket:
            try:
                data = self.client_socket.recv(1024)
                if data:
                    print(f"Received from module: {data.hex()}")  # Print as hex
                    print(f"ASCII: {data.decode('ascii', errors='replace')}")  # Print as ASCII
                else:
                    print("Client disconnected")
                    break
            except Exception as e:
                print(f"Receive error: {e}")
                break
    
    def send_data(self):
        """Send data to the 2-CH module"""
        while self.is_running and self.client_socket:
            try:
                message = input("Enter message to send (or 'quit' to exit): ")
                if message.lower() == 'quit':
                    self.stop_server()
                    break
                
                # Send as bytes
                self.client_socket.send(message.encode() + b'\n')  # Add newline
                print(f"Sent: {message}")
                
            except Exception as e:
                print(f"Send error: {e}")
                break
    
    def stop_server(self):
        """Stop the server and clean up"""
        self.is_running = False
        if self.client_socket:
            self.client_socket.close()
        if self.socket:
            self.socket.close()
        print("Server stopped")

# Simple version without threads
def simple_tcp_server():
    HOST = '192.168.1.100'
    PORT = 1000
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Simple TCP Server listening on {HOST}:{PORT}")
        
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                # Receive data
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received: {data.hex()}")
                print(f"Text: {data.decode('ascii', errors='replace')}")
                
                # Echo back (optional)
                # conn.sendall(data)


if __name__ == "__main__":
    print("Choose mode:")
    print("1. Interactive TCP Server with send/receive")
    print("2. Simple TCP Server (receive only)")
    
    choice = input("Enter choice (1 or 2): ")
    
    if choice == "1":
        server = TCPBridgeServer()
        try:
            server.start_server()
        except KeyboardInterrupt:
            print("\nServer interrupted by user")
            server.stop_server()
    else:
        simple_tcp_server()