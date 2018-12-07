"""TCP client example.
send numbers to a server and display the calculation.
"""

import socket as s
SIZE_LIMIT = 1024

SERVER_ADDR, SERVER_PORT = '127.0.0.1', 9000

sock = s.socket(s.AF_INET, s.SOCK_STREAM)

#input('wait')
sock.connect( (SERVER_ADDR, SERVER_PORT) )

print('Here is',sock.getsockname())

firstreply = sock.recv(SIZE_LIMIT)
firsti = int.from_bytes(firstreply,'big')
print('I am player{}'.format(firsti+1))
print('Input move in "x, y" format.')

if(firsti == 1):
    print("Waiting player1 to make the first move")
    reply = sock.recv(SIZE_LIMIT)
    i = int.from_bytes(reply,'big')
    print('Player1 made move {}'.format(i))

while True:
    val=int(input('Make a move (0 to quit):'))
    if val==0: break
    sock.send(val.to_bytes(4,'big'))
    print("...waiting player{} to make move...".format(2-firsti))

    reply = sock.recv(SIZE_LIMIT)
    i = int.from_bytes(reply,'big')
    print('Player{} made move {}'.format(2-firsti, i))

sock.close()
