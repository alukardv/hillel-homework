import asyncio

clients = []


async def process_socket(reader, writer):
    clients.append(writer)
    print(clients)

    while not reader.at_eof():
        message = await reader.read(100)
        print(message)
        for writer in clients:
            if not writer.is_closing():
                writer.write(message)
                await writer.drain()

    print('disconnected')
    writer.close()

async def main():
    server = await asyncio.start_server(process_socket, '0.0.0.0', 8887)
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)

    print(f'Server on {addrs}')
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())

