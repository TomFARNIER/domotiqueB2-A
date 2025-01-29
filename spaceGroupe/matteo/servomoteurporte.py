import machine
import time

servo_pin = machine.Pin(4)
pwm = machine.PWM(servo_pin, freq=50)

def set_angle(angle, sleepTime):
    """Définit l'angle du servomoteur."""
    duty = int((angle / 180) * 102 + 26)
    pwm.duty(duty)
    time.sleep(sleepTime)


# CODE POUR UTILISER SERVOMOTEUR
# while True:
#     set_angle(angle=0, sleepTime= 0.5)
#     set_angle(angle=90, sleepTime= 1)
