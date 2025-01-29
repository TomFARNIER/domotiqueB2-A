from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(26), freq=50)
def openWindow():
    """
    Ouvre la porte en réglant le servo sur une position spécifique.
    Cette fonction ajuste le rapport cyclique (duty cycle) du servo à 70,
    ce qui correspond à l'ouverture de la fenêtre. Elle attend ensuite 1 seconde
    pour permettre au servo de se stabiliser.
    """
    servo.duty(70)
    sleep(1)
    
def closeWindow():
    """
    Ferme la porte en réglant le servo sur une position spécifique.
    Cette fonction ajuste le rapport cyclique (duty cycle) du servo à 20,
    ce qui correspond à la fermeture de la fenêtre. Elle attend ensuite 1 seconde
    pour permettre au servo de se stabiliser.
    """
    servo.duty(20)
    sleep(1)