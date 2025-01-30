from __libs__ import Pin, sleep

class GazController:
    """
    Classe pour contrôler un capteur de gaz, une LED et un ventilateur.

    Attributes:
        gas_pin (Pin): Pin du capteur de gaz.
        led_pin (Pin): Pin de la LED indiquant l'état de la détection de gaz.
        ventilo_pin (Pin): Pin du ventilateur à activer en cas de détection de gaz.
    """

    def __init__(self, gazpin, ledpin, ventilopin):
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

    def eteindre_led(self):
        """Éteint la LED."""
        self.led_pin.off()

    def allumer_ventilo(self):
        """Allume le ventilateur."""
        self.ventilo_pin.value(1)

    def eteindre_ventilo(self):
        """Éteint le ventilateur."""
        self.ventilo_pin.value(0)

    def detecter_gaz(self):
        """
        Vérifie l'état du capteur de gaz et contrôle la LED et le ventilateur.

        Returns:
            bool: True si du gaz est détecté, False sinon.
        """
        gas_val = self.gas_pin.value()
        if gas_val == 1:  # Si du gaz est détecté
            self.allumer_led()  # Allume la LED
            self.allumer_ventilo()  # Allume le ventilateur
            return True
        else:  # Si aucun gaz n'est détecté
            self.eteindre_led()  # Éteint la LED
            self.eteindre_ventilo()  # Éteint le ventilateur
            return False
