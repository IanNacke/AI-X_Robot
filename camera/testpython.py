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
        print from_client
        parseMotorMessage(data)
        conn.send("server image data")
    conn.close()
    print 'client disconnected'