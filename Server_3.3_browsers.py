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
        data_received = message.split(b'\r\n')
        requested_resource = data_received[0].split(b' ')[1]

        if requested_resource == "/text/gasbot_sepia.png".encode(encoding='utf_8'):  # if the requested url is the image
            print(requested_resource)
            f = open(requested_resource[1:], 'rb')  # open the file at the url
            outputdata = f.read()   # read the file content
            connectionSocket.sendall(outputdata)    # send the file content
        else:
            requested_resource = "/text/text_only.html".encode(encoding='utf_8')  # for firefox we send text_only.html
            if str(message).find("Firefox") == -1:  # if the browser is not firefox
                requested_resource = "/text/image_only.html".encode(encoding='utf_8')  # we send image_only.html

            print(requested_resource)
            f = open(requested_resource[1:], 'rb')  # open the file at the url
            outputdata = f.read()   # read the file content
            connectionSocket.sendall(outputdata)    # send the file content

    except IOError:
        # ----------------------------------
        #       I/O Error handling
        # ----------------------------------
        print("404 not found")
        data = "<html><head></head><body><h1>404 not found</h1></body></html>\r\n"  # simple html string displaying "404 not found"
        connectionSocket.send(data.encode(encoding='utf_8'))    # send the html string
        connectionSocket.close()
    except IndexError:
        print('Index error exception')
serverSocket.close()
