from __libs__ import Pin, sleep

class Bouton:
    """
    Classe pour représenter un bouton.

    Attributes:
        pin (Pin): Instance de Pin configurée pour le bouton.
    """

    def __init__(self, pin):
        """
        Initialise et configure l'objet Pin pour le bouton.

        Args:
            pin (int): Le numéro du pin auquel le bouton est connecté.
        """
        self.pin = Pin(pin, Pin.IN, Pin.PULL_UP)

    def est_presse(self):
        """
        Vérifie si le bouton est pressé.

        Returns:
            bool: True si le bouton est pressé, False sinon.
        """
        if self.pin.value() == 0:  # Si le bouton est pressé (valeur 0)
            sleep(0.1)  # Anti-rebond
            return True
        sleep(0.1)  # Anti-rebond
        return False
