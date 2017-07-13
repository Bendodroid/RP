#!/usr/bin/env python3.5

# Copyright Bendodroid [2017]


import socket
import threading
import queue
import tc

from FileHandler import *


class ServerNetworkConnector:
    fd_name_match = dict()
    name_fd_match = dict()
    clientinfo = dict()
    cl_inf_broad = False
    conn = None
    addr = None
    start_receive_thread = None

    def __init__(self, nclients):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = input(tc.align_string("Enter your IP: ", 3))
        self.port = int(input(tc.align_string("Enter a port: ", 3)))
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        self.conns = []
        self.messageObjQueue = queue.Queue()
        self.start_client_thread = threading.Thread(target=self.acceptclients(nclients))
        self.start_client_thread.setDaemon(True)
        self.start_client_thread.start()

    def acceptclients(self, nclients: int):
        while True:
            if len(self.conns) < nclients:
                self.conn, self.addr = self.sock.accept()
                self.conns.append(self.conn)
                self.start_receive_thread = threading.Thread(target=self.receive, args=self.conn)
                self.start_receive_thread.setDaemon(True)
                self.start_receive_thread.start()

    def receive(self, conn):
        while True:
            try:
                msg = conn.recv(1024).decode("utf-8")
                if msg == "":
                    self.conns.remove(conn)
                    break
                # print("   Message received from: " + str(conn.getpeername()) + ": " + msg + ", " + str(conn))
                self.messageObjQueue.put([msg, conn.getpeername(), conn])
            except ConnectionResetError as e:
                print(e)
                pass

    def relay(self, msg_obj):
        for conn in self.conns:
            if not conn.getpeername() == msg_obj[1]:
                conn.sendall(msg_obj[0].encode("utf-8"))

    def broadcast(self, msg: str):
        for conn in self.conns:
            conn.sendall(msg.encode("utf-8"))

    def get_next_message_obj(self):
        return self.messageObjQueue.get()

    def send(self, msg: str, dest: str):
        for conn in self.conns:
            if self.fd_name_match[conn.fileno()] == dest:
                conn.sendall(msg.encode("utf-8"))

    def match_fd(self, msg: list):
        for sock in self.conns:
            if sock.fileno() == msg[2].fileno():
                self.fd_name_match[msg[2].fileno()] = json.loads(msg[0])["$NAME"]

    def rev_fd_list(self):
        for key, value in self.fd_name_match.items():
            self.name_fd_match[value] = key

    def dist_client_info(self):
        self.clientinfo = {
            "fd_name_match": self.fd_name_match,
            "name_fd_match": self.name_fd_match,
        }
        self.broadcast(json.dumps(self.clientinfo))


def main():
    # Create header
    tc.create_header("RP-API by Bendodroid  -  Server Version", clearterm=True)

    # Start Server
    nclients = int(input(tc.align_string("How many clients are allowed?: ", 3)))
    server = ServerNetworkConnector(nclients)

    # Server-Info
    print("\n")
    tc.create_infobox("Server-Info", "~", 3, False)
    print("\n" + tc.align_string("Server-Address: ", 3) + str(server.host))
    print(tc.align_string("Server-Port: ", 3) + str(server.port) + "\n\n")

    # Waiting for clients
    while True:
        if len(server.conns) == nclients:
            server.broadcast(json.dumps({"$ALL_CONN": True}))
            break

    print(server.conns)  # Kontrolle

    # Starting relay
    while True:
        msgobj = server.get_next_message_obj()
        msg = json.loads(msgobj[0])
        print("   ", msgobj)
        if msg["@RECIPIENT"] is not "@ALL":
            if msg["@RECIPIENT"] == "@SERVER":
                if msg["$TYPE"] == "$FD_MATCH" and len(server.fd_name_match) < nclients:
                    server.match_fd(msgobj)
                if len(server.fd_name_match) == nclients and server.cl_inf_broad is False:
                    server.rev_fd_list()
                    server.dist_client_info()
                    server.cl_inf_broad = True
            else:
                server.send(msg, msgobj["@RECIPIENT"])
        else:
            server.relay(msgobj)


main()
