"""TCP client example.
send numbers to a server and display the calculation.
"""

import socket as s
import base64
from gomoku import Gomoku
from board import Board
from player import Player

SIZE_LIMIT = 1024

SERVER_ADDR, SERVER_PORT = '127.0.0.1', 9000

sock = s.socket(s.AF_INET, s.SOCK_STREAM)

sock.connect( (SERVER_ADDR, SERVER_PORT) )

print('Here is',sock.getsockname())

firstreply = sock.recv(SIZE_LIMIT)
firsti = int.from_bytes(firstreply,'big')
print('I am player{}'.format(firsti+1))
print('Input move in "x, y" format.')


game = Gomoku()

if(firsti == 1):#firsti ==  means it is player2.
    print("Waiting player1 to make the first move")
    reply = sock.recv(SIZE_LIMIT)
    reply_dec = reply.decode('utf-8')
    if reply_dec == 'q':
        print("Player1 quits. Game end.")
        sock.close()
    print('Player1 made move {}'.format(reply_dec))
    game.play(reply_dec, firsti)#player 1 make play.

while True:
    strinput = input('Make a move (q to quit):')
    if strinput != 'q':
        playvalue = game.play(strinput, firsti+1)
        while playvalue == 0:
            strinput = input('Make a move (q to quit):')
            playvalue = game.play(strinput, firsti+1)
        if(playvalue == 1):
            strinput = "Player {} wins".format(firsti+1)
    else:
        playvalue = 1


    str_enc = strinput.encode('utf-8')

    sock.send(str_enc)
    if playvalue == 1: break
    print("...waiting player{} to make move...\n".format(2-firsti))





    reply = sock.recv(SIZE_LIMIT)
    reply_dec = reply.decode('utf-8')
    if reply_dec == 'q': break

    if (reply_dec == "Player 1 wins") or (reply_dec == "Player 2 wins"):
        print(reply_dec)
        break

    print('Player{} made move {}'.format(2-firsti, reply_dec))
    game.play(reply_dec, 2-firsti)
sock.close()
