import asyncio

HOST = "127.0.0.1"
PORT = 8080


async def send_message(writer, nickname):
    writer.write(nickname.encode())
    await writer.drain()

    while True:
        message = await asyncio.to_thread(input, "")
        if not message:
            continue

        writer.write(message.encode())
        await writer.drain()

        if message == "/exit":
            break


async def receive_message(reader):
    while True:
        data = await reader.read(1024)
        if not data:
            print("\nСоединение с сервером разорвано.")
            break
        print(data.decode(), end="")


async def main():
    nickname = input("Введите ваш никнейм: ")

    try:
        reader, writer = await asyncio.open_connection(HOST, PORT)
        print(f"Подключено к серверу как {nickname}")
        print("Команды: /users - список людей, /exit - выйти")

        await asyncio.wait(
            [
                asyncio.create_task(send_message(writer, nickname)),
                asyncio.create_task(receive_message(reader))
            ],
            return_when=asyncio.FIRST_COMPLETED
        )
    except ConnectionRefusedError:
        print("Ошибка: Сервер не запущен!")
    finally:
        print("Чат закрыт.")


if __name__ == "__main__":
    asyncio.run(main())
