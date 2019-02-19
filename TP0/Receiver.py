import asyncio
import os
import json

from Functs import cifrar,decifrar

password = "Some password"

@asyncio.coroutine
def handle_echo(reader,writer):
    data = yield from reader.read(1024)
    e = data.decode()
    mess = json.loads(e)
    texto = decifrar(mess,password) 
    #message = data.decode()
    addr = writer.get_extra_info('peername')
    print("%s -> %s" % (texto, addr))

def run_server():
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handle_echo,'127.0.0.1',9999, loop=loop)
    server = loop.run_until_complete(coro)
    #Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    #Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
    print('FINISHED!')

run_server()