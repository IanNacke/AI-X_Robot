  GNU nano 3.2                                                                                                                       server.py

import RPi.GPIO as GPIO
import pygame
import pygame.camera
import sys
import time
#import paramiko
import pathlib
import socketio

motorForward = 2
motorBackward = 3

def setupPins():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(motorForward, GPIO.OUT)
    GPIO.setup(motorBackward, GPIO.OUT)

    # Start both pins at LOW, which stops the motor from moving
    GPIO.output(motorForward, 0)
    GPIO.output(motorBackward, 0)

setupPins()

sio = socketio.Client()
sio.connect('http://1920.lakeside-cs.org:6544/')

@sio.on('controls message')
def controls(data):
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


#ssh_client=paramiko.SSHClient()
#ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh_client.connect(hostname='1920.lakeside-cs.org',username='student1920',password='m545CS41920')

controlsname="controlinfo"
imagename=str('webcamshot.jpg')
localpath=str(str(pathlib.Path().absolute()))
remotepath=str('/home/student1920/1920.lakeside-cs.org/public/Pall-Pareek/CS5Project/camera')

pygame.init()
pygame.camera.init()
#webcam = pygame.camera.Camera("/dev/video1",(160,120), "RGB")
webcam = pygame.camera.Camera(pygame.camera.list_cameras()[0], (160,120), "RGB")
webcam.start()

if webcam is None:
        sys.stdout.write("rip webcam \n")
else:
        sys.stdout.write("webcam is real \n")

#ftp_client=ssh_client.open_sftp()
while True:
        img = webcam.get_image()
        data = pygame.image.tostring(img,"RGB")
        sio.emit('image message', data)
#       pygame.image.save(img, imagename)
#       ftp_client.put(localpath+"/"+imagename, remotepath+"/"+imagename)
#       ftp_client.get(remotepath+"/"+controlsname, localpath+"/"+controlsname)
        time.sleep(0.1)

#ftp_client.close()


