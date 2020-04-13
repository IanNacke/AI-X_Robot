import socket,os
from PIL import *
import pygame,sys
import pygame.camera
import base64
from pygame.locals import *

sys.stdout.write("Helloo worldddd \n")
#Create server:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('10.0.0.101',5000))
server.listen(5)

#Start Pygame
pygame.init()
pygame.camera.init()

#screen = pygame.display.set_mode((320,240))
#cam = pygame.camera.Camera("/dev/video0",(320,240),"RGB")
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()

#Send data
while True:
    c, add = server.accept()
#    sys.stdout.write("Connected from " + ''.join(add) + "\n")
#    screen.blit(image,(0,0))
    #sys.stdout.write(cam.get_raw() + "\n")
    image = cam.get_raw()
    data_64 = base64.b64encode(image)
    c.sendall(data_64)
#    pygame.display.update()

#Interupt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
