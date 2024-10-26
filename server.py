import socket
import threading

IP = "127.0.0.1"
PORT = 8080

def recieve_messsage():
    """Recieve a message from the client"""

def unpack_message_protocol():
    """Unpack a message by the given protocol."""
    pass

def send_chat_message():
    """Send a broadcast message."""
    pass

def promote_a_user():
    """Give a specific user admin premissions(admin only command)"""
    pass

def kick_user():
    """Kick a specific user(admin only command)."""
    pass

def mute_user():
    """Mute a specific user(admin only command)."""
    pass

def private_message():
    "Send a private message for a specific user."
    pass

def start_server():
    """Start the server and handle new clients."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(10)

    print(f"Created a server at {IP}:{PORT}")

    #A while loop to create a thread for each new client.
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from: {client_address}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()


def handle_client():
    """Handle all of the server's major tasks for each client."""
    pass