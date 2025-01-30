from __libs__ import sleep, Pin ,I2cLcd
from machine import SoftI2C

class LCDDisplay:
    """
    Classe pour gérer l'affichage sur un écran LCD avec des caractères personnalisés.
    """




    def __init__(self, pin_scl, pin_sda):
        """
        Initialise l'écran LCD avec des caractères personnalisés.

        Args:
            lcd: Instance de l'écran LCD à utiliser.
        """
        self.custom_chars = {
            "thermometer": bytearray([0x04, 0x0A, 0x0A, 0x0A, 0x0A, 0x1B, 0x1F, 0x0E]),
            "umbrella": bytearray([0x00, 0x04, 0x0E, 0x1F, 0x04, 0x04, 0x14, 0x0C]),
            "porte": bytearray([0x1F, 0x1F, 0x1F, 0x1F, 0x1D, 0x1F, 0x1F, 0x1F]),
            "rfid": bytearray([0x00, 0x00, 0x0E, 0x11, 0x04, 0x0A, 0x00, 0x04]),
            "nuke": bytearray([0x0E, 0x15, 0x1F, 0x0A, 0x0E, 0x0E, 0x00, 0x00]),
            "ventilo1": bytearray([0x00, 0x02, 0x14, 0x0E, 0x05, 0x08, 0x00, 0x00]),
            "ventilo2": bytearray([0x00, 0x08, 0x0B, 0x04, 0x1A, 0x02, 0x00, 0x00]),
            "fenetre": bytearray([0x00, 0x00, 0x00, 0x1F, 0x15, 0x1F, 0x15, 0x1F])
        }
        self.i2c = SoftI2C(scl=Pin(pin_scl), sda=Pin(pin_sda), freq=10000)
        self.I2C_ADDR = 0x27
        self.totalRows = 2
        self.totalColumns = 16
        self.lcd = I2cLcd(self.i2c, self.I2C_ADDR, self.totalRows, self.totalColumns)
        self.initialize_custom_chars()

    def initialize_custom_chars(self):
        """Initialise les caractères personnalisés sur l'écran LCD."""
        for index, char in enumerate(self.custom_chars.values()):
            self.lcd.custom_char(index, char)

    def afficher_dht(self, temperature, humidity):
        """Affiche la température et l'humidité sur l'écran LCD."""
        self.lcd.clear()
        self.lcd.putstr(f"{chr(0)} T: {temperature} C")
        self.lcd.move_to(0, 1)
        self.lcd.putstr(f"{chr(1)} H: {humidity} %")
        sleep(2)

    def afficher_gas(self):
        """Affiche l'état du gaz sur l'écran LCD avec une animation."""
        self.lcd.clear()
        self.lcd.putstr(f"{chr(2)} Gas: OUI")
        self.lcd.move_to(0, 1)

        while True:
            for i in range(3, 5):  # Indices 3 and 4 correspond to ventilo1 and ventilo2
                self.lcd.move_to(0, 1)
                self.lcd.putchar(" ")
                self.lcd.move_to(0, 1)
                self.lcd.putchar(chr(i))
                sleep(0.2)

    def afficher_rfid(self, is_valid=True):
        """Affiche l'état du RFID sur l'écran LCD."""
        self.lcd.clear()
        self.lcd.putstr(f"{chr(5)} RFID: {'Bon' if is_valid else 'Pas bon'}")

    def afficher_trou(self, windows_open=False, door_open=False):
        """Affiche l'état de la fenêtre et de la porte sur l'écran LCD."""
        self.lcd.clear()
        self.lcd.putstr(f"{chr(6)} Fenetre: {'Open' if windows_open else 'Closed'}")
        self.lcd.move_to(0, 1)
        self.lcd.putstr(f"{chr(7)} Porte: {'Open' if door_open else 'Closed'}")

    def clear(self):
        """Efface l'écran LCD."""
        self.lcd.clear()
