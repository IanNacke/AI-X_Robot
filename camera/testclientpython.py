# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:06:40 2020

@author: IanN20
"""


import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('10.0.0.146', 6432))

while True:
    client.send(b'client control data')
    server_image_data = client.recv(4096)
    print(server_image_data)
client.close()