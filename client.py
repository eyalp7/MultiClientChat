import socket
import threading

IP = "127.0.0.1"
PORT = 8080

def get_a_username():
    """Get a valid username from the client."""
    username = input("Enter your username(avoid using @ at the start or using more than 16 characters): ")

    #A while loop that iterates untill the username is valid
    while len(username) > 16 or username[0] == '@':
        if len(username) > 16:
            print("This username is too long! ")
        if username[0] == '@':
            print("Try a username that doesn't start with @! ")
        username = input("Try a new username: ")

def connect_to_server():
    """Connect to the chat server."""
    client_socket = socket.socket()
    client_socket.connect((IP, PORT))

    #Create a thread for recieving threads and sending commands to the server.
    commands_thread = threading.Thread(target=send_a_command).start()
    recieving_thread = threading.Thread(target=recieve_a_message).start()

    #Wait for the threads to finish their task.
    commands_thread.join()
    recieving_thread.join()

    
def recieve_a_message():
    """Recieve a message from the server."""
    pass

def pack_a_message():
    """Pack a message by the given protocol"""
    pass

def send_a_command():
    """Send a specific command following the given protocol."""
    pass



