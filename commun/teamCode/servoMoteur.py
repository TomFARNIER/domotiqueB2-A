from __libs__ import sleep , PWM, Pin

class ServoMotor:
    """
    Classe représentant un servomoteur.

    Attributes:
        servo_pin (Pin): Pin utilisé pour contrôler le servomoteur.
        pwm (PWM): Objet PWM associé au servomoteur.
    """

    def __init__(self, pin):
        """
        Initialise le servomoteur.

        Args:
            pin (int): Le numéro du pin auquel le servomoteur est connecté.
        """
        self.servo_pin = Pin(pin)
        self.pwm = PWM(self.servo_pin, freq=50)

    def set_angle(self, angle, sleep_time):
        """
        Définit l'angle du servomoteur.

        Args:
            angle (int): L'angle à régler (0 à 180 degrés).
            sleep_time (float): Temps d'attente après le réglage de l'angle, en secondes.
        """
        duty = int((angle / 180) * 102 + 26)
        self.pwm.duty(duty)
        sleep(sleep_time)


