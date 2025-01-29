import time
import machine
from machine import Pin, SoftI2C
import esp32



# Récupère le pin côté out
p0 = Pin(18, Pin.OUT)


def AllumerLed(_pin):
    _pin.on()


def EteindreLed(_pin):
    _pin.off()


MOTOR_PIN = Pin(17, Pin.OUT)


def AllumerVentilo(_motorPin):
    _motorPin.value(1)


def EteindreVentilo(_motorPin):
    _motorPin.value(0)


gas = Pin(26, Pin.IN, Pin.PULL_DOWN)


def GazController(LedPin, VentiloPin):
    #Fonction qui permet de détecter le gaz, gère la led et le ventilo
    while True:
        gasVal = gas.value()
        print("gas =", gasVal)
        if gasVal == 1: # si il y a du gaz
            print("Je suis mort y a du gaz les gars ptdrr")
            AllumerLed(LedPin) # allume la led
            AllumerVentilo(VentiloPin) # allume le ventilo
        else: # si il n'y a pas de gaz
            print("y a pas de gaz")
            EteindreLed(LedPin) # éteint la led
            EteindreVentilo(VentiloPin) # éteint le ventilo
        time.sleep(0.2)
