#!/usr/bin/env python3

import socket
import sys
import threading
from queue import Queue

print_lock = threading.lock()
q = Queue()

# TCP Scanner


def scanner(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        remote_server = input('Enter a remote host to scan:')
        remote_server_IP = socket.gethostbyname(remote_server)
        result = sock.connect_ex((remote_server_IP, port))

        if result == 0:
            print('Port {}: OPEN'.format(port))
        sock.close()

        except socket.error:
            print('Could not connect to server')
            sys.exit()

        except KeyboardInterrupt:
            print('Exiting...')
            sys.exit()


def threader():
    while True:
        port = q.get()
        scanner(port)
        q.task_done


def main():
    for x in range(100):
        thread = threading.Thread(target=threader)
        thread.daemon = True
        thread.start()

    for port in range(100):
        q.put(port)

    q.join()


if __name__ == '__main__':
    for port in range(100):
        scanner(port)
