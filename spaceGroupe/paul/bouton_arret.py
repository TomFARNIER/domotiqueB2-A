from machine import Pin, PWM
from time import sleep

# Définition du bouton avec résistance de pull-up activée
button = Pin(12, Pin.IN, Pin.PULL_UP)

def isBoutonArretGeneralPressed():
    """
    Vérifie si le bouton d'arrêt général est pressé.

    Retourne :
        bool : True si le bouton est pressé, False sinon.
    """
    if button.value() == 0:
        sleep(0.1)
        return True
    sleep(0.1)
    return False

while True:
    if isBoutonArretGeneralPressed():  # Vérifie si le bouton est pressé
        print("Bouton pressé !")  # Ajoute une action visible
    sleep(0.1)  # Délai pour éviter une boucle trop rapide
