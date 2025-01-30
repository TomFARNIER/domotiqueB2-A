from __libs__ import NeoPixel, Pin, randint, time, sleep

class CapteurMouvement:
    """
    Classe pour gérer un capteur de mouvement et des LEDs RGB.

    Attributes:
        capteur (Pin): Instance du capteur de mouvement.
        led_rgb (NeoPixel): Instance des LEDs RGB contrôlées par le capteur.
    """

    def __init__(self, capteur_mouvement_pin : int, led_rgb_pin : int , num_leds : int):
        """
        Initialise le capteur de mouvement et les LEDs RGB.

        Args:
            capteur_mouvement_pin (int): Le numéro du pin auquel le capteur de mouvement est connecté.
            led_rgb_pin (int): Le numéro du pin auquel les LEDs RGB sont connectées.
            num_leds (int): Le nombre de LEDs RGB à contrôler.
        """
        self.capteur = Pin(capteur_mouvement_pin, Pin.IN)
        self.led_rgb = NeoPixel(Pin(led_rgb_pin), num_leds)

    def couleur_aleatoire(self):
        """
        Génère une couleur RGB aléatoire.

        Returns:
            tuple: Un tuple contenant trois valeurs entières représentant une couleur RGB.
        """
        return (randint(0, 255), randint(0, 255), randint(0, 255))

    def mode_disco(self, duree: float=5 ):
        """
        Fait clignoter les LED en mode disco pendant une durée donnée (en secondes).

        Args:
            duree (int): La durée pendant laquelle les LEDs clignotent, par défaut 5 secondes.
        """
        start_time = time()
        while time() - start_time < duree:
            for i in range(len(self.led_rgb)):
                self.led_rgb[i] = self.couleur_aleatoire()
                sleep(0.1)
            self.led_rgb.write()
            sleep(0.2)
        self.eteindre_led_rgb()
        sleep(1)

        return None

    def eteindre_led_rgb(self):
        """
        Éteint toutes les LED RGB.
        """
        for i in range(len(self.led_rgb)):
            self.led_rgb[i] = (0, 0, 0)
            sleep(0.1)
        self.led_rgb.write()
        sleep(1)
        return None

    def getValeurCapteur(self) -> int:
        """
        Renvoie la valeur du capteur de mouvement.

        Returns:
            int: La valeur du capteur de mouvement (0 ou 1).
        """
        return self.capteur.value()
