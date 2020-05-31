import io
import pygame
import sys
from PIL import Image
import time
import paramiko
import pathlib

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='1920.lakeside-cs.org',username='student1920',password='m545CS41920')
ftp_client=ssh_client.open_sftp()

imagename=str('webcamshot.jpg')
localpath=str(str(pathlib.Path().absolute())+"\\"+imagename)
remotepath=str('/home/student1920/1920.lakeside-cs.org/public/Pall-Pareek/CS5Project/camera'+"/"+imagename)

pygame.init();

# trying to figure out image_stream-this doesn't really do much yet
image_stream = io.BytesIO();

#setting the variables for the UI, getting width height and setting colors
width = 1200;
height = 800;

streamWidth = 320*2;
streamHeight = 240*2;

black = (0,0,0);
white = (255,255,255);
#starting the game display
gameDisplay = pygame.display.set_mode((width,height));
pygame.display.set_caption('Wireless Controller');
#setting fps variable to whatever fps we want to run at
fps = 100;
#setting up the loop which will run while the controller is still running
clock = pygame.time.Clock();
crashed = False;
#getting the images for the keys that will appear on the board
wImg = pygame.image.load('w.png');
wDownImg = pygame.image.load('wDown.png');
aImg = pygame.image.load('a.png');
aDownImg = pygame.image.load('aDown.png');
sImg = pygame.image.load('s.png');
sDownImg = pygame.image.load('sDown.png');
dImg = pygame.image.load('d.png');
dDownImg = pygame.image.load('dDown.png');
image = pygame.image
previousimage = pygame.image
FPS =0
fStart = time.time()
fEnd = time.time()
#declaring the fucntion for each key which either displays the normal key image
# or the image of it toggled depending on variable <letter>down
#displays at passed in coordinates
def w(x,y,wDown):
    if(wDown):
        gameDisplay.blit(wDownImg,(x,y));
    else:
        gameDisplay.blit(wImg, (x,y));
def a(x,y,aDown):
    if(aDown):
        gameDisplay.blit(aDownImg,(x,y));
    else:
        gameDisplay.blit(aImg, (x,y));
def s(x,y,aDown):
    if(sDown):
        gameDisplay.blit(sDownImg,(x,y));
    else:
        gameDisplay.blit(sImg, (x,y));
def d(x,y,aDown):
    if(dDown):
        gameDisplay.blit(dDownImg,(x,y));
    else:
        gameDisplay.blit(dImg, (x,y));
def videoImg(x,y,image):
    gameDisplay.blit(image,(x,y));
#setting the variables for where the keys are going to go on the screen
# and setting the down variables to false
xW = int((width*0.48));
yW = int((height*0.7));
wDown = False;
xA = int((width*0.4));
yA = int((height*0.8));
aDown = False;
xS = int((width*0.48));
yS = int((height*0.8));
sDown = False;
xD = int((width*0.56));
yD = int((height*0.8));
dDown = False;
# these variables are set to false and will just look at if the key is down
wKeyDown = False;
aKeyDown = False;
sKeyDown = False;
dKeyDown = False;
#width and height of the buttons
buttonWidth = 57;
buttonHeight = 51;
#creating the mouse and click objects
mouse = pygame.mouse.get_pos();
click = pygame.mouse.get_pressed();
# sendArray is the array we will send to the rasberry pi
#index 0 is w, index 1 is a, index 2 is s, and index 3 is d
sendArray = [0,0,0,0];
#button checks if a mouse is a. over the selected area and b. clicking
#returns boolean down to say if it is down or not
def button(x,y):
    mouse = pygame.mouse.get_pos();
    click = pygame.mouse.get_pressed();
    down = False;
    if buttonWidth+x > mouse[0] >x and buttonHeight+y >mouse[1]>y:
        if click[0] == 1:
            down = True;
        else:
            down = False;
    else:
        down = False;
    return down;
# the loop
while not crashed:    
    # gets all the events
    for event in pygame.event.get():
        #sets <letter>ButtonDown to the boolean from button for each key
        wButtonDown = button(xW,yW);
        aButtonDown = button(xA,yA);
        sButtonDown = button(xS,yS);
        dButtonDown = button(xD,yD);
        # if pygame gets closed it stops the loop
        if  event.type == pygame.QUIT:
            crashed = True;
        # if a key is down, it checks if w,a,s,or d are down and sets <that leter>keyDown to true
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                wKeyDown = True;
            if event.key == pygame.K_a:
                aKeyDown = True;
            if event.key == pygame.K_s:
                sKeyDown = True;
            if event.key == pygame.K_d:
                dKeyDown = True;
        # whenever a key comes up it does the same thing as for keydown but sets the boolean to false if that key came up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                wKeyDown = False;
            if event.key == pygame.K_a:
                aKeyDown = False;
            if event.key == pygame.K_s:
                sKeyDown = False;
            if event.key == pygame.K_d:
                dKeyDown = False;
        # goes through each key and sets the <letter>Down boolean to down if key or button is down
        # also changes sendArray at each index for each key changes it to 1 if it is down or 0 if it is not
        if wButtonDown or wKeyDown:
            wDown = True;
            sendArray[0] = 1;
        elif not wButtonDown and not wKeyDown:
            wDown = False;
            sendArray[0] = 0;
        if aButtonDown or aKeyDown:
            aDown = True;
            sendArray[1] = 1;
        elif not aButtonDown and not aKeyDown:
            aDown = False;
            sendArray[1] = 0;
        if sButtonDown or sKeyDown:
            sDown = True;
            sendArray[2] = 1;
        elif not sButtonDown and not sKeyDown:
            sDown = False;
            sendArray[2] = 0;
        if dButtonDown or dKeyDown:
            dDown = True;
            sendArray[3] = 1;
        elif not dButtonDown and not dKeyDown:
            dDown = False;
            sendArray[3] = 0;
    # |||
    # VVV testing for image stream
    
    ftp_client.get(remotepath, localpath);
    videoImg = pygame.image.load(imagename);
    #print(localpath);
    
    # sets background to white
    gameDisplay.fill(white);
    # puts all the keys on the board
    w(xW,yW,wDown);
    a(xA,yA,aDown);
    s(xS,yS,sDown);
    d(xD,yD,dDown);
    videoImage(100,100,videoImg);
    #videoImage()
    #again testing VVV
    #updates the screen
    pygame.display.update();
    #tells pygame how many frames per second to run at, caluclates how many miliseconds between each frame
    clock.tick(fps);
# closes pygame
pygame.quit();
