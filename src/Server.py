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
    gamemaster = None

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nclients = int(input(tc.align_string("How many clients are allowed?: ", 3)))
        self.host = input(tc.align_string("Enter your IP: ", 3))
        self.port = int(input(tc.align_string("Enter a port: ", 3)))
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        self.conns = []
        self.messageObjQueue = queue.Queue()
        self.start_client_thread = threading.Thread(target=self.acceptclients)
        self.start_client_thread.setDaemon(True)
        self.start_client_thread.start()

    def acceptclients(self):
        print("\n\n")
        tc.create_infobox("Server-Info", "~", 3, False)
        print("\n" + tc.align_string("Server-Address: ", 3) + self.host)
        print(tc.align_string("Server-Port: ", 3) + str(self.port) + "\n")
        print(tc.print_message("Waiting for Clients to connect...", "INFO"))
        while True:
            if len(self.conns) < self.nclients:
                self.conn, self.addr = self.sock.accept()
                self.conns.append(self.conn)
                self.start_receive_thread = threading.Thread(target=self.receive, args=(self.conn,))
                self.start_receive_thread.setDaemon(True)
                self.start_receive_thread.start()
            else:
                pass

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
                if json.loads(msg[0])["$GAMEMASTER"] is True and self.gamemaster is None:
                    self.gamemaster = sock.fileno()

    def rev_fd_list(self):
        for key, value in self.fd_name_match.items():
            self.name_fd_match[value] = key

    def dist_client_info(self):
        self.clientinfo = {
            "fd_name_match": self.fd_name_match,
            "name_fd_match": self.name_fd_match,
            "gamemaster": self.fd_name_match[self.gamemaster],
        }
        self.broadcast(json.dumps(self.clientinfo))


def main():
    # Create header
    tc.create_header("RP-API by Bendodroid  -  Server Version", clearterm=True)
    tc.set_term_title("RP-API - Server")

    # Start Server
    server = ServerNetworkConnector()

    # Waiting for clients
    while True:
        if len(server.conns) == server.nclients:
            server.broadcast(json.dumps({"$ALL_CONN": True}))
            break

    # Starting relay
    while True:
        msgobj = server.get_next_message_obj()
        try:
            msg = json.loads(msgobj[0])
            print("   ", msgobj)
            if msg["$RECIPIENT"] != "ALL":
                if msg["$RECIPIENT"] == "SERVER":
                    if msg["$TYPE"] == "FD_MATCH" and len(server.fd_name_match) < server.nclients:
                        server.match_fd(msgobj)
                    if len(server.fd_name_match) == server.nclients and server.cl_inf_broad is False:
                        server.rev_fd_list()
                        server.dist_client_info()
                        server.cl_inf_broad = True
                else:
                    server.send(msgobj[0], msg["$RECIPIENT"])
            else:
                server.relay(msgobj)
        except json.JSONDecodeError:
            pass


main()
