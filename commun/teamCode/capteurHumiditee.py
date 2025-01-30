from __libs__ import DTH, Pin

class CapteurHumidite:
    """
    Classe pour gérer un capteur d'humidité DHT11.

    Attributes:
        dht (DTH): Instance du capteur DHT11 connectée à une broche spécifique.
    """

    def __init__(self, pin: int):
        """
        Initialise le capteur DHT11 sur la broche spécifiée.

        Args:
            pin (int): Numéro de la broche où est connecté le capteur DHT11.
        """
        self.dht = DTH(Pin(pin), 0)  # 0 pour DHT

    def mesurer(self) -> int:
        """
        Effectue une mesure de l'humidité et détermine si elle dépasse un seuil.

        Returns:
            int: 1 si l'humidité est supérieure ou égale à 40 %, sinon 0.
        """
        result = self.dht.read()  # Lire les données du capteur
        if result.is_valid():  # Vérifiez si les données sont valides
            print(f"Température : {result.temperature}°C, Humidité : {result.humidity}%")
            return 1 if result.humidity >= 40 else 0
        else:
            print("Erreur lors de la lecture du capteur")
            return 0

