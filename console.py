import pygame
import socket

host = '172.20.10.7';
port = 65432;
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
SOCKET.connect((host,port));
pygame.init();


width = 1200;
height = 800;
black = (0,0,0);
white = (255,255,255);

gameDisplay = pygame.display.set_mode((width,height));
pygame.display.set_caption('Wireless Controller');
clock = pygame.time.Clock();
crashed = False;
wImg = pygame.image.load('w.png');
wDownImg = pygame.image.load('wDown.png');
aImg = pygame.image.load('a.png');
aDownImg = pygame.image.load('aDown.png');
sImg = pygame.image.load('s.png');
sDownImg = pygame.image.load('sDown.png');
dImg = pygame.image.load('d.png');
dDownImg = pygame.image.load('dDown.png');
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
wKeyDown = False;
aKeyDown = False;
sKeyDown = False;
dKeyDown = False;
buttonWidth = 57;
buttonHeight = 51;
mouse = pygame.mouse.get_pos();
click = pygame.mouse.get_pressed();
sendString = '';
sendArray = [0,0,0,0];
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
while not crashed:
    for event in pygame.event.get():
        wButtonDown = button(xW,yW);
        aButtonDown = button(xA,yA);
        sButtonDown = button(xS,yS);
        dButtonDown = button(xD,yD);
        if  event.type == pygame.QUIT:
            crashed = True;
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                wKeyDown = True;
            if event.key == pygame.K_a:
                aKeyDown = True;
            if event.key == pygame.K_s:
                sKeyDown = True;
            if event.key == pygame.K_d:
                dKeyDown = True;
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                wKeyDown = False;
            if event.key == pygame.K_a:
                aKeyDown = False;
            if event.key == pygame.K_s:
                sKeyDown = False;
            if event.key == pygame.K_d:
                dKeyDown = False;
        if wButtonDown or wKeyDown:
            wDown = True;
            sendString = 'F'
            sendArray[0] = 1;
        elif not wButtonDown and not wKeyDown:
            wDown = False;
            sendString = '0'
            sendArray[0] = 0;
        if aButtonDown or aKeyDown:
            aDown = True;
            sendString = sendString + 'L';
            sendArray[1] = 1;
        elif not aButtonDown and not aKeyDown:
            aDown = False;
            sendString = sendString + '0';
            sendArray[1] = 0;
        if sButtonDown or sKeyDown:
            sDown = True;
            sendString = sendString + 'B';
            sendArray[2] = 1;
        elif not sButtonDown and not sKeyDown:
            sDown = False;
            sendString = sendString + '0';
            sendArray[2] = 0;
        if dButtonDown or dKeyDown:
            dDown = True;
            sendString = sendString + 'R';
            sendArray[3] = 1;
        elif not dButtonDown and not dKeyDown:
            dDown = False;
            sendString = sendString + '0';
            sendArray[3] = 0;
        SOCKET.sendall(bytes(sendArray))
        

        #print(event);
    gameDisplay.fill(white);
    w(xW,yW,wDown);
    a(xA,yA,aDown);
    s(xS,yS,sDown);
    d(xD,yD,dDown);
    pygame.display.update();
    clock.tick(60);
pygame.quit();
guit();
