from __libs__ import Pin, sleep

class GazController:
    """
    Classe pour contrôler un capteur de gaz, une LED et un ventilateur.

    Attributes:
        gas_pin (Pin): Pin du capteur de gaz.
        led_pin (Pin): Pin de la LED indiquant l'état de la détection de gaz.
        ventilo_pin (Pin): Pin du ventilateur à activer en cas de détection de gaz.
    """

    def __init__(self, gazpin:int, ledpin:int, ventilopin:int):
        """
        Initialise le GazController avec les pins spécifiés.

        Args:
            gazpin (int): Le numéro du pin du capteur de gaz.
            ledpin (int): Le numéro du pin de la LED.
            ventilopin (int): Le numéro du pin du ventilateur.
        """
        self.gas_pin = Pin(gazpin, Pin.IN)
        self.led_pin = Pin(ledpin, Pin.OUT)
        self.ventilo_pin = Pin(ventilopin, Pin.OUT)

    def allumer_led(self):
        """Allume la LED."""
        self.led_pin.on()
        sleep(1)
        return None

    def eteindre_led(self):
        """Éteint la LED."""
        self.led_pin.off()
        sleep(1)
        return None

    def allumer_ventilo(self):
        """Allume le ventilateur."""
        self.ventilo_pin.value(1)
        sleep(1)
        return None

    def eteindre_ventilo(self):
        """Éteint le ventilateur."""
        self.ventilo_pin.value(0)
        sleep(1)
        return None

    def detecter_gaz(self) -> bool:
        """
        Vérifie si du gaz est détecté.

        Returns:
            bool: True si du gaz est détecté, False sinon.
        """
        return self.gas_pin.value() == 1


