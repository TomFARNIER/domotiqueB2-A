from __libs__ import sleep
from commun.teamCode.servoMoteur import ServoMotor

class Porte(ServoMotor):
    """
    Classe représentant une porte contrôlée par un servomoteur.

    Attributes:
        ouverte (bool): Indique si la porte est ouverte ou fermée.
    """

    def __init__(self, pin:int):
        """
        Initialise la porte avec le pin du servomoteur.

        Args:
            pin (int): Le numéro du pin auquel le servomoteur de la porte est connecté.
        """
        super().__init__(pin)
        self.ouverte = False

    def ouvrir(self):
        """
        Ouvre la porte si elle est fermée.

        La méthode ajuste l'angle du servomoteur pour ouvrir la porte.
        Si la porte est déjà ouverte, rien ne se passe.
        """
        if not self.ouverte:
            self.set_angle(90, 1)  # Ajustez l'angle pour ouvrir
            self.ouverte = True
            sleep(1)
        return None

    def fermer(self):
        """
        Ferme la porte si elle est ouverte.

        La méthode ajuste l'angle du servomoteur pour fermer la porte.
        Si la porte est déjà fermée, rien ne se passe.
        """
        if self.ouverte:
            self.set_angle(0, 1)  # Ajustez l'angle pour fermer
            self.ouverte = False
            sleep(1)
        return None
