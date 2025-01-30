from __libs__ import MFRC522, Pin, sleep ,SPI


class RFIDReader:
    """
    Classe pour gérer la lecture des cartes RFID.

    Attributes:
        spi (SPI): Instance de SPI pour la communication avec le module RFID.
        rdr (MFRC522): Instance de MFRC522 pour interagir avec le module RFID.
        target_card_id (str): ID de la carte RFID cible à détecter.
    """

    def __init__(self, sck=18, mosi=23, miso=19, rst=2, cs=21, target_card_id="0x5a3dafb6"):
        """
        Initialise le lecteur RFID.

        Args:
            sck (int): Numéro de la broche SCK. Défaut: 18
            mosi (int): Numéro de la broche MOSI. Défaut: 23
            miso (int): Numéro de la broche MISO. Défaut: 19
            rst (int): Numéro de la broche RST. Défaut: 2
            cs (int): Numéro de la broche CS. Défaut: 21
            target_card_id (str): ID de la carte RFID cible. Défaut: "0x5a3dafb6"
        """
        self.spi = SPI(2, baudrate=115200, polarity=0, phase=0, sck=Pin(sck), mosi=Pin(mosi), miso=Pin(miso))
        self.rdr = MFRC522(spi=self.spi, gpioRst=rst, gpioCs=cs)
        self.target_card_id = target_card_id

    def log_error(self, message):
        """Affiche un message d'erreur."""
        print(f"[ERROR] {message}")

    def log_info(self, message):
        """Affiche un message d'information."""
        print(f"[INFO] {message}")

    def rfidCheck(self)->int:
        """
        Lit les cartes RFID.

        Returns:
            str: "authorized" si la carte cible est détectée, "error" si une autre carte est détectée, "unknown" si aucune carte n'est détectée.
        """
        while True:
            try:
                (stat, tag_type) = self.rdr.request(self.rdr.REQALL)
                if stat != self.rdr.OK:
                    return 1

                self.log_info("Carte détectée. Tentative d'anticollision...")
                (stat, raw_uid) = self.rdr.anticoll()
                if stat != self.rdr.OK:
                    self.log_error("Échec de l'anticollision. Réessayez.")
                    sleep(1)
                    continue

                card_id = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
                self.log_info(f"Carte lue avec succès: {card_id}")

                if card_id == self.target_card_id:
                    return 1
                else:
                    return 0

            except Exception as e:
                self.log_error(f"Erreur inattendue: {e}")

            sleep(1)


