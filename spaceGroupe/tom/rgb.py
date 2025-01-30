import time
import random
import machine
from machine import PWM, Pin, I2C
from neopixel import NeoPixel
import esp32

capteur_mouvement_pin = 23
capteur_mouvement = Pin(capteur_mouvement_pin, Pin.IN)

led_rgb_pin = 2
led_rgb = NeoPixel(Pin(led_rgb_pin), 4)

def couleur_aleatoire():
    """Génère une couleur RGB aléatoire."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def mode_disco(duree=5):
    """Fait clignoter les 4 LED en mode disco pendant une durée donnée (en secondes)."""
    start_time = time.time()
    while time.time() - start_time < duree:
        for i in range(4):
            led_rgb[i] = couleur_aleatoire()
        led_rgb.write()
        time.sleep(0.2)
    eteindre_led_rgb()

def eteindre_led_rgb():
    """Éteint toutes les LED RGB."""
    for i in range(4):
        led_rgb[i] = (0, 0, 0)
    led_rgb.write()

while True:
    if capteur_mouvement.value() == 1:  # Détection de mouvement
        print(" Mouvement détecté ! Mode Disco activé ")
        mode_disco(5)  # Mode disco pendant 5 secondes
    else:
        eteindre_led_rgb()

    time.sleep(0.1)