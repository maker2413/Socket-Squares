"""
*********************************************************
*                                                       *
* Project Name: Socket Squares                          *
* Author: github.com/kirigaine                          *
* Description: A simple socket project with pygame,     *
*   each player controls a randomly generated square    *
*   and can see eachother's movement.                   *
* Requirements: TBD                                     *
*                                                       *
*********************************************************
"""
import socket
import threading
from queue import Queue
import pickle
from random import randint

#import square as sq

# Server network constants
SERVERIP = socket.gethostbyname(socket.gethostname())
PORT = 26256

# Server data constraints
HEADER_SIZE = 16
FORMAT_TYPE = 'utf-8'

# Create and bind server socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((SERVERIP,PORT))

square_array = []

def clientHandling(client_conn, client_addr, array):
    # Boolean to manage connection status for server
    connected = True
    print(f"[SERVER] Connection established @ {client_addr[0]}:{PORT}")
    while connected:

        # Receive header that describes data length
        header_data = client_conn.recv(HEADER_SIZE).decode(FORMAT_TYPE)

        # If data has any content/exists, process the data
        if header_data:
            # Convert the header to an integer to use to receive exact amount of data
            header_data = int(header_data)
            data = client_conn.recv(header_data).decode(FORMAT_TYPE)
            # If data is specific message, disconnect client
            #d = pickle.loads(data)
            #data = d
            if data == "!quit":
                connected = False
                print(f"{client_addr} has disconnected")
            # Print data if not attempt to disconnect
            else:
                print (f"[{client_addr}] says: {data}")
            header_data = data = ""
            # Send confirmation message to client
            client_conn.send("Data received".encode(FORMAT_TYPE))

    # Disconnect client
    client_conn.close() 

def squareHandler():
    squares = []

    def addSquare(new_square):
        squares.append(new_square)

def serverLaunch():
    # Start socket listening
    print("[SERVER] Server is launching...")
    #square_thread = threading.Thread(target=squareHandler)
    #square_thread.start()
    # Limit total amount of clients connected
    server.listen(8)
    print(f"[SERVER] Server is listening at {SERVERIP} on port {PORT}")

    #q = Queue()

    while True:
        # If a client attempts to connect, accept and store connection and address
        client_conn, client_addr = server.accept()
        # Create a thread and pass method to handle client
        thread = threading.Thread(target=clientHandling, args=((client_conn,client_addr,square_array)))
        thread.start()
        # Display current amount of users when someone connects
        print(f"[SERVER] Current Users: {threading.activeCount() - 1}")



serverLaunch()