from gpiozero import MotionSensor, LED, Buzzer, Button
from time import sleep
from signal import pause

pir = MotionSensor(26)
buzzer = Buzzer(19)
button = Button(13)
led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(10)
led5 = LED(9)
led6 = LED(11)
    
all = [led1,led2,led3,led4,led5,led6]

def all_on():
    buzzer.on()
    for i in all:
        i.on()
        sleep(0.1)
    

def all_off():
    buzzer.off()
    for i in all:
        i.off()
while True:
    button.wait_for_press()
    print("SYSTEM ARMED YOU HAVE 5 SECONDS TO RUN AWAY")
    sleep(5)
    pir.when_motion = all_on
    pir.when_no_motion = all_off	
