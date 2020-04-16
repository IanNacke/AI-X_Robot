import socket
import pygame
import pygame.camera
import sys
import time

port = 5432
#textport = 6543
pygame.init()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(("10.0.0.217",port))
serversocket.listen(1)

#textsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#textsocket.bind(("10.0.0.101",textport))
#textsocket.listen(1)

pygame.camera.init()
webcam = pygame.camera.Camera("/dev/video1",(160,120), "RGB")
if webcam is None:
	sys.stdout.write("rip webcam \n")
else:
	sys.stdout.write("webcam is real \n")

webcam.start()

while True:
        connection, address = serversocket.accept()
        image = webcam.get_image() # capture image
        data = pygame.image.tostring(image,"RGB") # convert captured image to string, use RGB color scheme
	connection.sendall(data)
        time.sleep(0.1)
        connection.close()
#	textconn, textaddr = textsocket.accept()
#	textconn.sendall("hell0")
#	textconn.close()
