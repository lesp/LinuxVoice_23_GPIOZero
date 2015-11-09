from gpiozero import MotionSensor, LED

pir = MotionSensor(26)
led = LED(17)

pir.when_motion = led.on
pir.when_no_motion = led.off
