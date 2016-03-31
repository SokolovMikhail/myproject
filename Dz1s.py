import socket
sock = socket.socket()
sock.bind(('localhost',8000))
sock.listen(5)
buf_size = 2048

while True:
    conn, addr = sock.accept()
    buf = conn.recv(buf_size)
    buf1 = buf.decode()
    path = buf1.split('\n')[0].split(' ')[1]
    path = path[1:]
    if path == "":
        path = "index.html"
    f = open(path, 'rb')
    conn.send(f.read())
    f.close()
    conn.close()
sock.close()
