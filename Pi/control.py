import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
in1=35
in2=37
in3=36
in4=38
enA=31
enB=32
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
ena=GPIO.PWM(enA,65)
enb=GPIO.PWM(enB,65)
ena.start(0)
enb.start(0)

def forward():
    GPIO.output(in1,1)
    GPIO.output(in2,0)
    GPIO.output(in3,1)
    GPIO.output(in4,0)

def backward():
    GPIO.output(in1,0)
    GPIO.output(in2,1)
    GPIO.output(in3,0)
    GPIO.output(in4,1)

def run():
    ena.ChangeDutyCycle(100)
    enb.ChangeDutyCycle(100)

def stop():
    ena.ChangeDutyCycle(0)
    enb.ChangeDutyCycle(0)

def right():
    ena.ChangeDutyCycle(100)
    enb.ChangeDutyCycle(50)

def left():
    ena.ChangeDutyCycle(50)
    enb.ChangeDutyCycle(100)

def turnR():
    ena.ChangeDutyCycle(100)
    enb.ChangeDutyCycle(0)

def turnL():
    ena.ChangeDutyCycle(0)
    enb.ChangeDutyCycle(100)

def spinR():
    GPIO.output(in1,1)
    GPIO.output(in2,0)
    GPIO.output(in3,0)
    GPIO.output(in4,1)
    ena.ChangeDutyCycle(100)
    enb.ChangeDutyCycle(100)

def spinL():
    GPIO.output(in1,0)
    GPIO.output(in2,1)
    GPIO.output(in3,1)
    GPIO.output(in4,0)
    ena.ChangeDutyCycle(100)
    enb.ChangeDutyCycle(100)

def move(x, move_time=0.1):
    if x=='w':
        forward()
        run()
    elif x=='e':
        forward()
        right()
    elif x=='q':
        forward()
        left()
    elif x=='d':
        forward()
        turnR()
    elif x=='a':
        forward()
        turnL()
    elif x=='s':
        backward()
        run()
    elif x=='x':
        backward()
        right()
    elif x=='z':
        backward()
        left()
    elif x=='j':
        spinL()
    elif x=='k':
        spinR()

    time.sleep(move_time)
    stop()

if __name__=='__main__':
    import readchar
    while True:
        try:
            x=readchar.readkey()
        except:
            ena.stop()
            enb.stop()
            GPIO.cleanup()
            break
        if x==' ':
            ena.stop()
            enb.stop()
            GPIO.cleanup()
            break
        move(x)
