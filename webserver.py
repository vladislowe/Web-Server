import socket

#get user's request
def parse_request(request):
    parsed = request.split(' ')
    req = parsed[1]
    return req

#send response to the user
def send_response(req, client_socket):
    if req == "/index.html" or req == "/":
        with open("index.html", "rb") as file:
            readfile = file.read()
            client_socket.send((f"HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Lenght: {len(readfile)}\n\n").encode())
            client_socket.send(readfile)
    elif req == "/github.png":
        with open("github.png", "rb") as file:
            readfile = file.read()
            client_socket.send((f"HTTP/1.1 200 OK\nContent-Type: image/png\nContent-Lenght: {len(readfile)}\n\n").encode())
            client_socket.send(readfile)
    elif req == "/background2.jpg":
        with open("background2.jpg", "rb") as file:
            readfile = file.read()
            client_socket.send((f"HTTP/1.1 200 OK\nContent-Type: image/jpg\nContent-Lenght: {len(readfile)}\n\n").encode())
            client_socket.send(readfile)
    else:
        client_socket.send((f"HTTP/1.1 404 Not found\n\n").encode())
        client_socket.send("<h1>404</h1><p>Not found</p>".encode())

#establish TCP connect
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 80))
server_socket.listen()

while True:
    print(70*'-')
    client_socket, addr = server_socket.accept()
    request = client_socket.recv(1024)
    request = request.decode('utf-8')
    print(request)
    print("Address: ", addr)
    print()
    req = parse_request(request) #file
    print("User`s requests: ", req)

    send_response(req, client_socket)

    client_socket.close()
