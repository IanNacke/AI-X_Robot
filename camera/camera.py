import pygame
import pygame.camera
import socket

pygame.init()
pygame.camera.init()
cameras = pygame.camera.list_cameras()
#cam = pygame.camera.Camera(cameras[0], (320,240), 'RGB')
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()

while True:
	s.add = server.accept
	data = cam.get_raw
	s.sendall(data)
