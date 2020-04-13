import RPi.GPIO as GPIO
import time
import socket
import pygame
import pygame.camera
import sys

motorForward = 2
motorBackward = 3

def setupPins():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(motorForward, GPIO.OUT)
    GPIO.setup(motorBackward, GPIO.OUT)

    # Start both pins at LOW, which stops the motor from moving
    GPIO.output(motorForward, 0)
    GPIO.output(motorBackward, 0)

def parseMotorMessage(data):
    return
    forward = data[0]
    backward = data[2]
    if not (forward ^ backward): # XOR
        GPIO.output(motorForward, 0)
        GPIO.output(motorBackward, 0)
        print('Stop!')
    elif data[0] == 1:
        GPIO.output(motorForward, 1)
        GPIO.output(motorBackward, 0)
        print('Forward!')
    elif data[2] == 1:
        GPIO.output(motorForward, 0)
        GPIO.output(motorBackward, 1)
        print('Backward!')


setupPins()

host = '10.0.0.101'
port = 65432
pygame.init()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((host ,port))
serversocket.listen(1)

pygame.camera.init()
webcam = pygame.camera.Camera("/dev/video1",(160,120), "RGB")
webcam.start()

print('Listening on host:',host,'port:',port)
while True:
	print("help")
	connection, address = serversocket.accept()
	print("Recieving data")
	data = connection.recv(1024)
        if not data:
	    print("Recieved invalid data - breaking")
            break
        print('recieved:', data, "\n")

        if data == b'Exit':
	    print("recieved exit code - breaking")
            break

        image = webcam.get_image() # capture image
        data = pygame.image.tostring(image,"RGB") # convert captured image to string, use RGB color scheme
        print("sending camera data")
	connection.sendall(data)
        time.sleep(0.1)
        connection.close()

        parseMotorMessage(data)


GPIO.cleanup()
