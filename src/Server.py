# Copyright Bendodroid [2017]


import socket
import threading
import queue
import tc

from FileHandler import *
from pprint import pprint


def main():
    # Create header
    tc.create_header("RP-API by Bendodroid  -  Server Version", clearterm=True)

    # Start Server

    server = ServerNetworkConnector()

    nclients = int(input(tc.align_string("How many clients are allowed?: ", 3)))

    # Server-Info
    print("\n")
    tc.create_infobox("Server-Info", "~", 3, False)
    print("\n" + tc.align_string("Server-Address: ", 3) + str(server.host))
    print(tc.align_string("Server-Port: ", 3) + str(server.port) + "\n\n")

    while True:
        if len(server.conns) == nclients:
            server.broadcast(json.dumps({"$ALL_CONN": True}))
            break

    print(server.conns)

    for i in range(nclients):
        msg = server.get_next_message_obj()
        server.match_ip(msg)

    server.match_conns()  # Hier weitermachen für Name-ip matches

    pprint(server.ip_name_match, indent=2)
    pprint(server.name_ip_match, indent=2)

    # print(tc.align_string("Starting relay...", 3))
    # while True:
    #     msg = server.get_next_message_obj()
    #     msgobj = json.loads(msg[0])
    #     print("   ", msg)
    #     if msgobj["@RECIPIENT"] is not "@ALL":
    #         if msgobj["@RECIPIENT"] == "@SERVER":
    #             if msgobj["$TYPE"] == "$IP_MATCHES":
    #                 server.ip_name_match = msgobj["$IP_MATCHES"]
    #                 server.match_conns()
    #         else:
    #             server.send(msg[0], msgobj["@RECIPIENT"])
    #     else:
    #         server.relay(msgobj)


###


class ServerNetworkConnector:
    ip_name_match = dict()
    name_ip_match = dict()

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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

    def send(self, msg, dest):
        pass

    def match_ip(self, msg):
        for sock in self.conns:
            print(sock)
            print(sock.fd)
            # if sock.raddr == msg[1]:
            #     self.ip_name_match[msg[1]] = json.loads(msg[0])["$NAME"]

    def match_conns(self):
        for key, value in self.ip_name_match.items():
            self.name_ip_match[value] = key

main()
