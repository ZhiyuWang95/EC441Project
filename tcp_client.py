"""TCP client example.
send numbers to a server and display the calculation.
"""

import socket as s
SIZE_LIMIT = 1024

SERVER_ADDR, SERVER_PORT = '127.0.0.1', 9000

sock = s.socket(s.AF_INET, s.SOCK_STREAM)

#input('wait')
sock.connect( (SERVER_ADDR, SERVER_PORT) )

print('i am',sock.getsockname())

while True:
    val=int(input('give me a number to factorialize (0 to quit):'))
    if val==0: break

    sock.send(val.to_bytes(4,'big'))
    reply = sock.recv(SIZE_LIMIT)
    i = int.from_bytes(reply,'big')
    print('{}! is'.format(val), i)

sock.close()