"""TCP server example.

Calculate factorials for clients.
"""
import math
import multiprocessing
import subprocess
import socket as s
from multiprocessing import Process, Pipe

SIZE_LIMIT = 16
SERVER_ADDR, SERVER_PORT = '127.0.0.1', 9000


server_soc = s.socket(s.AF_INET, s.SOCK_STREAM)

server_soc.bind( (SERVER_ADDR, SERVER_PORT) )
server_soc.listen(1)
print('Server is listening.')
clients = []
connections = []
parentpip = []

def handle(connection, address, conn):
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("process-%r" % (address,))
    try:
        logger.debug("Connected %r at %r", connection, address)
        while True:
            message = connection_soc.recv(SIZE_LIMIT)
            val = int.from_bytes(message,'big')
            if not val: break

            fact_res = message #changed by ZY.
            #msg = fact_res.to_bytes(12,'big')
            conn.send(fact_res)
    except:
        logger.exception("Problem handling request")

def sendIndex(connection, clients):
    index = len(clients)
    index_msg = index.to_bytes(12,'big')
    connection_soc.send(index_msg)

while True:
    if(len(clients) < 2):
        connection_soc, addr = server_soc.accept()
        info_pair = (connection_soc, addr)
        sendIndex(connection_soc, clients)

        if(info_pair not in clients):
            clients.append(info_pair)
            connections.append(connection_soc)

            parent_conn, child_conn = Pipe()

            parentpip.append(parent_conn)
            process = multiprocessing.Process(target=handle, args=(connection_soc, addr, child_conn))
            process.daemon = True
            process.start()
            print('responding to ', addr)
    else:
        player1 = parentpip[0].recv()
        if(player1):
            move1 = player1
            connections[1].send(move1)
            if move1.decode('utf-8') == 'q':
                print('player1 quit, game over.')
                break

        player2 = parentpip[1].recv()
        if(player2):
            move2 = player2
            connections[0].send(move2)
            if move2.decode('utf-8') == 'q':
                print('player2 quit, game over.')
                break


for i in range(2):
    connections[i].close()
connections.clear()
