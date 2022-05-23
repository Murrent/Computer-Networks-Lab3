# Martin Vickgren
# Import socket module
from socket import *

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 80

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

while True:
    print('Waiting for requests ...')
    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()
    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    try:
        message = connectionSocket.recv(1024)
        # -------------------------------------------
        #       Request handling Section
        # -------------------------------------------

        data = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(data.encode(encoding='utf_8'))
        data = "<html><head></head><body><h1>Hello world!</h1></body></html>\r\n"
        connectionSocket.send(data.encode(encoding='utf_8'))

        print('A new request has been received...')
        print(message)
        # Close the client connection socket
        connectionSocket.close()

    except IOError:
        # ----------------------------------
        #       I/O Error handling
        # ----------------------------------
        connectionSocket.close()
#       else:
#               print('An exception has occured')

serverSocket.close()
