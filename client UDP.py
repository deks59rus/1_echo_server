import socket
import threading
import time

def receive_messages():
    while True:
        try:
            data, _ = sock.recvfrom(1024)
            print(f"Message from server: {data.decode('utf-8')}")
        except OSError:
            print("Сокет закрыт. Выход из потока получения сообщений.")
            break

def connect_to_server():
    while True:
        try:
            sock.connect((host, port))
            print("Успешно подключено к серверу.")
            break
        except (ConnectionRefusedError, OSError):
            print(f"Не удалось подключиться к серверу {host}:{port}. Повторная попытка через 5 секунд...")
            time.sleep(5)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = 'localhost'
port = 12345

# Попытка подключения к серверу
connect_to_server()

# Запуск потока для получения сообщений
threading.Thread(target=receive_messages, daemon=True).start()

while True:
    msg = input("Ваше сообщение (введите 'exit' для выхода): ")
    if msg.lower() == 'exit':
        print("Вы отключаетесь от сервера...")
        break
    try:
        sock.sendto(msg.encode('utf-8'), (host, port))
        print("Сообщение отправлено на сервер.")
    except OSError as e:
        print(f"Ошибка при отправке сообщения: {e}")

sock.close()
print("Соединение с сервером закрыто.")
