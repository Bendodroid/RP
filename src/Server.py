# Copyright Bendodroid [2017]

import socket
import threading
import queue

from tc import align_string


def main():
    pass


class ServerNetworkConnector:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = input(align_string("Enter your IP: ", 3))
        self.port = int(input(align_string("Enter a port: ", 3)))
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        self.conns = []
        self.messageObjQueue = queue.Queue()
        self.start_client_thread = threading.Thread(target=self.acceptclients)
        self.start_client_thread.setDaemon(True)
        self.start_client_thread.start()

    def acceptclients(self):
        while True:
            self.conn, self.addr = self.sock.accept()
            self.conns.append(self.conn)
            self.start_receive_thread = threading.Thread(target=self.receive, args=(self.conn,))
            self.start_receive_thread.setDaemon(True)
            self.start_receive_thread.start()

    def receive(self, conn):
        while True:
            try:
                msg = conn.recv(1024).decode("utf-8")
                if msg == "":
                    self.conns.remove(conn)
                    break
                # print("message received from " + str(conn.getpeername()) + ": " + msg)
                self.messageObjQueue.put((msg, conn.getpeername()))
            except ConnectionResetError as e:
                print(e)
                pass

    def relay(self, msg_obj):
        for conn in self.conns:
            if not conn.getpeername() == msg_obj[1]:
                conn.sendall(msg_obj[0].encode("utf-8"))

    def broadcast(self, msg):
        for conn in self.conns:
            conn.sendall(msg.encode("utf-8"))

    def get_next_message_obj(self):
        return self.messageObjQueue.get()
