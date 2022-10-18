#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

host = '127.0.0.1'
port = 9999


def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serversocket.connect((host, port))

    a = ''

    while a != '/stop':
        server_responсe = serversocket.recv(1024)

        print(server_responсe.decode('utf-8'))

        a = input()

        serversocket.send(a.encode('utf-8'))

        server_responсe = serversocket.recv(1024)

        print(server_responсe.decode('utf-8'))

    print('Connection closed!')


if __name__ == '__main__':
    main()
