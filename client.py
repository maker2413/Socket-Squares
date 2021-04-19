"""
client.py
"""
# Standard library
import socket
import re
import pickle
import sys

# Third party
import pygame
#from pygame.sprite import Group

# Local source
import game_functions as gf
import square

# Server port, IPv4 will be prompted
PORT = 26256

# Server data constraints
HEADER_SIZE = 16
FORMAT_TYPE = 'utf-8'

def main():
    server_ip = ipPrompt()

    # Create and connect client socket
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((server_ip,PORT))

    # Report to client that connection has been established with server
    print(f"[SERVER] You have connected to the server @ {server_ip}")

    # Initialize and manage pygame settings
    print("Launching game window...")
    pygame.init()
    pygame.display.set_caption("Socket Squares")

    # Declare pygame screen and resolution
    screen = pygame.display.set_mode((800,600))

    # !!! Receive the exact amount of data rather than 2048
    print("Receiving character data...")
    my_square = client.recv(2048)
    my_square = pickle.loads(my_square)
    my_square = square.PlayerSquare(my_square, screen)
    print("Character data received.")

    # List of all current player squares
    squares = []

    while True:

        gf.check_events(screen, my_square)
        print(f"X: {my_square.h_velocity} Y: {my_square.y_velocity} RECT: {my_square.rect.center}")
        #pickleSwap(my_square,client)
        gf.update_screen(screen, my_square)



        # Infinitely request and send input until keyword entered, then disconnect
        """myinput = ""
        while myinput != "!quit" and myinput != "!q":
            myinput = input("Say: ")
            dataSwap(myinput, client)
        else:
            client.close()
            print("You have disconnected from the server. Now exiting...")
            pygame.quit()
            break"""
    else:
        client.close()
        print("You have disconnected from the server. Now exiting...")
        pygame.quit()
        sys.exit()



def ipPrompt():
    # Prompt user for IPv4, determine if given IPv4 is "valid" using regex. Don't continue until pass regex
    temp_ipv4 = ""
    regex_passed = None
    while not regex_passed:
        temp_ipv4 = input("\nEnter the IPv4 Address of a server to connect to: ")
        regex_passed = re.search("^[0-9]{1,3}\.{1}[0-9]{1,3}\.{1}[0-9]{1,3}\.{1}[0-9]{1,3}$", temp_ipv4)
        if not regex_passed:
            print("Invalid IPv4. Please try again following the format: X.X.X.X")
    return temp_ipv4

def dataSwap(data, client):

    # Encode string in utf-8
    alldata = data.encode(FORMAT_TYPE)

    # Add buffer and encode data length string in utf-8 
    send_length = f"{len(alldata):<{HEADER_SIZE}}"
    send_length = str(send_length).encode(FORMAT_TYPE)

    # Send header to server, then data
    client.send(send_length)
    client.send(alldata)

    # Receive data from server
    return (client.recv(2048).decode(FORMAT_TYPE))

def pickleSwap(data, client):
    alldata = pickle.dumps(square.MySquare(data.player_id, data.name))
    send_length = f"{len(alldata):<{HEADER_SIZE}}"
    send_length = str(send_length).encode(FORMAT_TYPE)

    client.send(send_length)
    client.send(alldata)

    squares = client.recv(2048)
    squares = pickle.loads(squares)

main()