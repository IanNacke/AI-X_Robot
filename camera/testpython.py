import socket
motorForward = 2
motorBackward = 3

def setupPins():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(motorForward, GPIO.OUT)
    GPIO.setup(motorBackward, GPIO.OUT)

    # Start both pins at LOW, which stops the motor from moving
    GPIO.output(motorForward, 0)
    GPIO.output(motorBackward, 0)
def isOn(data):
    if data == 1:
        return true
    else:
        return false

def parseMotorMessage(data):
    return
    forward = isOn(data[0])
    backward = isOn(data[2])
    left = isOn(data[1])
    right = isOn(data[3])
    if forward and not backward and not left and not right: # XOR
        GPIO.output(motorForward, 1)
        GPIO.output(motorBackward, 0)
        print('Forward!')
    elif not forward and backward and left and not right:
        GPIO.output(motorForward, 0)
        GPIO.output(motorBackward, 1)
        print('Backward!')
    elif not forward and not backward and left and not right:
        GPIO.output(motorForward, 1)
        GPIO.output(motorBackward, 0)
        print('Left!')
    elif not forward and not backward and not left and right:
        GPIO.output(motorForward, 0)
        GPIO.output(motorBackward, 1)
        print('Right!')
    elif forward and left and not backward and not right:
        GPIO.output(motorForward, 1)
        GPIO.output(motorBackward, 0)
        print('Forward and Left!')
    elif forward and right and not backward and not left:
        GPIO.output(motorForward, 0)
        GPIO.output(motorBackward, 0)
        print('Forward and Right!')
    elif backward and left and not forward and not right:
        GPIO.output(motorForward, 0)
        GPIO.output(motorBackward, 0)
        print('Backward and Left!')
    elif backward and right and not forward and not left:
        GPIO.output(motorForward, 0)
        GPIO.output(motorBackward, 1)
        print('Backward and Right!')
    else:
        GPIO.output(motorForward, 0)
        GPIO.output(motorBackward, 0)
        print('Not moving')

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('10.0.0.146', 6432))
serv.listen(5)
setupPins()
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break

        from_client += data
        print (from_client)
        parseMotorMessage(data)
        conn.send("server image data")
    conn.close()
    print ('client disconnected')
