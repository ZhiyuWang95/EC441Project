"""TCP client example.
send numbers to a server and display the calculation.
"""

import socket as s
import base64

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
    reply_dec = reply.decode('utf-8')
    if reply_dec == 'q':
        print("Player1 quits. Game end.")
        sock.close()
    print('Player1 made move {}'.format(reply_dec))

while True:
    #val=int(input('Make a move (0 to quit):'))
    strinput = input('Make a move (q to quit):')
    str_enc = strinput.encode('utf-8')

    sock.send(str_enc)
    if strinput=='q': break
    print("...waiting player{} to make move...\n".format(2-firsti))

    reply = sock.recv(SIZE_LIMIT)
    reply_dec = reply.decode('utf-8')
    if reply_dec == 'q': break

    print('Player{} made move {}'.format(2-firsti, reply_dec))

sock.close()
