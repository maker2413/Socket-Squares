﻿# Socket-Squares

## Description

Socket-Squares is a simple pygame application that allows users to connect to a server and see eachother move their randomly generated squares around. This application is a means for me to learn and use sockets without following a complete tutorial. I have zero experience with netcode for a "game" up until now, so systems likely have better implementations.

## Installation

You should only need python and the pygame library to run Socket-Squares. The pip package manager can be used as such to install the requirements:
```bash
pip install -r requirements.txt
```

## Usage

1. Run server.py on the desired host
   - ```python server.py```
2. Clients run client.py and enter the IPv4 of the desired server *(Note: Up to 8 clients may connect to a server at a time)*
   - ```python client.py```
3. Press 'ESC' key to exit the client at any time.

## Controls

Control your square using WASD or the arrow keys

## Known Issues

1. The socket has multiple ways to fail connecting over the internet. Make sure to port forward 26256 TCP for your router, check your firewall, and consider other standard errors when hosting/connecting online.

2. The older commits have an issue opening and reading *names.txt* inside the SquareFactory class when running *server.py*. This is an error on my part due to my workspace hierarchy, and it will prevent the server from running unless you setup your file architecture like mine. However, the better fix is to simply alter the code (if for some reason you want to run the oldest working version). The fix:

    **Original *square.py*, line 27**
    ```python
    with open("python\\testing\\socket_squares\\names.txt", "r") as f:
    ```

    **Corrected *square.py*, line 27**
    ```python
    with open("names.txt", "r") as f:
    ```

## Contributing

This is a project for me to learn. While I'm not entirely against pull requests, I don't want everything completed and fixed for me. Minor changes are acceptable,
but opening an issue is likely a better way for something to get fixed. Thanks!

## Authors and acknowledgment

Kirigaine - Developer

A quick thanks to [maker2413](https://github.com/maker2413) for teaching me about requirements.txt and .python-version.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Project Status

This project is still ongoing.
