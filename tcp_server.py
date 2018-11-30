"""TCP server example.

Calculate factorials for clients.
"""
import math
import socket as s

SIZE_LIMIT = 16
SERVER_ADDR, SERVER_PORT = '127.0.0.1', 9000


server_soc = s.socket(s.AF_INET, s.SOCK_STREAM)

server_soc.bind( (SERVER_ADDR, SERVER_PORT) )
server_soc.listen(1)
print('Server is listening.')

while True:
    connection_soc, addr  = server_soc.accept()
    print('responding to ', addr)
    while True:
        message =  connection_soc.recv(SIZE_LIMIT)
        val = int.from_bytes(message,'big')
        if not val: break

        fact_res = math.factorial(val)
        msg = fact_res.to_bytes(12,'big')
        connection_soc.send(msg)

    connection_soc.close()
    print('done')