import asyncio
import aiofiles

# Задание 1

async def async_counter(n):
    for i in range(1, n + 1):
        print(f"Число: {i}")
        await asyncio.sleep(1)

async def main():
    print("Старт счетчика...")
    await async_counter(5)
    print("Счетчик завершил работу.")

if __name__ == '__main__':
    asyncio.run(main())

# Задание 2

async def download_file_1():
    await asyncio.sleep(3)
    print("File 1 downloaded")

async def download_file_2():
    await asyncio.sleep(2)
    print("File 2 downloaded")

async def download_file_3():
    await asyncio.sleep(1)
    print("File 3 downloaded")

async def main():
    print("Загрузка началась...")
    await asyncio.gather(
        download_file_1(),
        download_file_2(),
        download_file_3()
    )

    print("Все файлы загружены!")

if __name__ == '__main__':
    asyncio.run(main())

# Задание 3

async def async_write_file(filename, text):
    async with aiofiles.open(filename, mode='w', encoding='utf-8') as f:
        await f.write(text)
        print(f"Файл {filename} успешно записан.")

async def async_read_file(filename):
    async with aiofiles.open(filename, mode='r', encoding='utf-8') as f:
        content = await f.read()
        print(f"Прочитано из {filename}: {content}")
        return content

async def main():
    files_to_write = [
        ("file1.txt", "Ехал Грека"),
        ("file2.txt", "Через реку"),
        ("file3.txt", "Видит Грека в реке рак")
    ]

    print("\n\tЗапись файлов")
    write_tasks = [async_write_file(name, txt) for name, txt in files_to_write]
    await asyncio.gather(*write_tasks)

    print("\n\tЧтение файлов")
    filenames = ["file1.txt", "file2.txt", "file3.txt"]
    read_tasks = [async_read_file(name) for name in filenames]
    await asyncio.gather(*read_tasks)

if __name__ == '__main__':
    asyncio.run(main())
