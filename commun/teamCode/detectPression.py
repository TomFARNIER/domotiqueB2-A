from time import sleep

from __libs__ import ADC, Pin

class DetectPression:
    """
    Classe pour détecter la pression à l'aide d'un capteur analogique.

    Attributes:
        adc (ADC): Instance de l'objet ADC configuré pour lire la valeur du capteur.
    """

    def __init__(self, pin: int):
        """
        Initialise et configure l'objet ADC pour un pin donné.

        Args:
            pin (int): Le numéro du pin auquel le capteur de pression est connecté.
        """
        self.adc = ADC(Pin(pin))
        self.adc.atten(ADC.ATTN_11DB)  # Plage de 0 à 3.3V pour ESP32

    def lire_valeur(self) -> bool:
        """
        Lit la valeur du capteur de pression.

        Cette méthode lit la valeur brute de l'ADC, la convertit en valeur DAC,
        et détermine si cette valeur est supérieure ou égale à un seuil.

        Returns:
            bool: True si la valeur est supérieure ou égale à 40, sinon False.
        """
        adc_val = self.adc.read()
        dac_val = round(adc_val * 255 / 4095)
        print(f"ADC Val: {adc_val}, \t DAC Val: {dac_val}")
        sleep(1)

        return dac_val >= 40
