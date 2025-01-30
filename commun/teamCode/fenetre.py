from __libs__ import sleep
from commun.teamCode.servoMoteur import ServoMotor

class Fenetre(ServoMotor):
    """
    Classe représentant une fenêtre contrôlée par un servomoteur.

    Attributes:
        ouverte (bool): Indique si la fenêtre est ouverte ou fermée.
    """

    def __init__(self, pin:int):
        """
        Initialise la fenêtre avec le pin du servomoteur.

        Args:
            pin (int): Le numéro du pin du servomoteur associé à la fenêtre.
        """
        super().__init__(pin)
        self.ouverte = False

    def ouvrir(self):
        """
        Ouvre la fenêtre si elle n'est pas déjà ouverte.

        Cette méthode règle l'angle du servomoteur pour ouvrir la fenêtre
        et met à jour l'état de la fenêtre.
        """
        if not self.ouverte:
            self.set_angle(70, 1)  # Ajustez l'angle pour ouvrir
            self.ouverte = True
        sleep(1)
        return None

    def fermer(self):
        """
        Ferme la fenêtre si elle est ouverte.

        Cette méthode règle l'angle du servomoteur pour fermer la fenêtre
        et met à jour l'état de la fenêtre.
        """
        if self.ouverte:
            self.set_angle(20, 1)  # Ajustez l'angle pour fermer
            self.ouverte = False
        sleep(1)
        return None