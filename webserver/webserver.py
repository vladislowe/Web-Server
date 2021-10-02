import socket

#get user's request
def parse_request(request):
    parsed = request.split(' ')
    try:
        req = parsed[1]
    except IndexError:
        return None
    return req

#send response to the user
def send_response(req, client_socket):
    if req == "/index.html" or req == "/":
        with open("/usr/src/app/index.html", "rb") as file:
            readfile = file.read()
            client_socket.send((f"HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Lenght: {len(readfile)}\n\n").encode())
            client_socket.send(readfile)
    elif req == "/github.png":
        with open("/usr/src/app/github.png", "rb") as file:
            readfile = file.read()
            client_socket.send((f"HTTP/1.1 200 OK\nContent-Type: image/png\nContent-Lenght: {len(readfile)}\n\n").encode())
            client_socket.send(readfile)
    elif req == "/background2.jpg":
        with open("/usr/src/app/background2.jpg", "rb") as file:
            readfile = file.read()
            client_socket.send((f"HTTP/1.1 200 OK\nContent-Type: image/jpg\nContent-Lenght: {len(readfile)}\n\n").encode())
            client_socket.send(readfile)
    else:
        client_socket.send((f"HTTP/1.1 404 Not found\n\n").encode())
        client_socket.send("<h1>404</h1><p>Not found</p>".encode())

def logs(request, req, addr):
    with open("/usr/src/app/webserver_logs.txt", "a") as file:
        file.write(70*'-')
        file.write(request)
        #print("Address: ", addr)
        file.write()
        file.write("User`s requests: ", req)
        
def main():
    #establish TCP connect
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 80))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        request = request.decode('utf-8')
        req = parse_request(request) #file
        logs(request, req, addr)

        send_response(req, client_socket)

        client_socket.close()

if __name__ == "__main__":
    main()
