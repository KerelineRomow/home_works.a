import asyncio

HOST = "127.0.0.1"
PORT = 8080

clients = {}

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info("peername")
    nickname = ""

    try:
        data = await reader.read(1024)
        if not data:
            return
        nickname = data.decode().strip()
        clients[nickname] = writer

        print(f"Подключился: {nickname} ({addr})")

        join_msg = f"{nickname} вошел в чат\n"
        for cw in clients.values():
            if cw != writer:
                cw.write(join_msg.encode())
                await cw.drain()

        while True:
            data = await reader.read(1024)
            if not data:
                break

            message = data.decode().strip()

            if message.startswith("/"):
                if message == "/users":
                    user_list = ", ".join(clients.keys())
                    response = f"В сети: {user_list}\n"
                    writer.write(response.encode())
                    await writer.drain()

                elif message == "/exit":
                    writer.write("Вы вышли из чата. До свидания!\n".encode())
                    await writer.drain()
                    break

                else:
                    writer.write("Неизвестная команда.\n".encode())
                    await writer.drain()

                continue

            broadcast_msg = f"[{nickname}]: {message}\n"
            print(f"Чат: {broadcast_msg.strip()}")

            for client_writer in clients.values():
                if client_writer != writer:
                    client_writer.write(broadcast_msg.encode())
                    await client_writer.drain()

    except Exception as e:
        print(f"Ошибка с пользователем {nickname}: {e}")
    finally:
        if nickname in clients:
            del clients[nickname]
            print(f"Отключился: {nickname}")

            leave_msg = f"{nickname} покинул чат\n"
            for cw in clients.values():
                cw.write(leave_msg.encode())
                await cw.drain()

        writer.close()
        await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    print(f"Сервер запущен на {HOST}:{PORT}")
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
