import socket
import pygame
import sys
from PIL import Image
import time

host = "10.0.0.103"
port=5432
width = 320*3
height = 240*3
screen = pygame.display.set_mode((width,height),0)
image = pygame.image
previousimage = pygame.image
FPS = 0
fStart = time.time()
fEnd = time.time()


while True:
    clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((host, port))
    received = []
    fStart = time.time()
    # loop .recv, it returns empty string when done, then transmitted data is completely received
    while True:
        #print("esperando receber dado")
        recvd_data = clientsocket.recv(230400)
        if not recvd_data:
            break
        else:
            received.append(recvd_data)

    dataset = b''.join(received)
    image = pygame.image.fromstring(dataset,(160,120),"RGB") # convert received image from string
    output = pygame.transform.scale(image, (width, height))
    screen.blit(output,(0,0)) # "show image" on the screen
    pygame.display.update()
    fEnd = time.time()
    print(str(int(1/(fEnd-fStart))) + " FPS")

    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()