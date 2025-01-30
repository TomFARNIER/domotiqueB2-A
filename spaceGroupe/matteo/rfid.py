from machine import Pin, SPI
from mfrc522 import MFRC522
from time import sleep


def log_error(message):
    print(f"[ERROR] {message}")


def log_info(message):
    print(f"[INFO] {message}")


sck = 18
mosi = 23
miso = 19
rst = 2
cs = 21

spi = SPI(2, baudrate=115200, polarity=0, phase=0, sck=Pin(sck), mosi=Pin(mosi), miso=Pin(miso))
rdr = MFRC522(spi=spi, gpioRst=rst, gpioCs=cs)


def RFID():
    """
    Fonction pour lire les cartes RFID
    
    Returns:
            bool: True si il détecte la bonne carte
            bool: False si il détecte une autre carte
            None: Si il n'y a pas de carte
    """
    while True:
        try:
            (stat, tag_type) = rdr.request(rdr.REQALL)
            if stat != rdr.OK:
                return None

            log_info("Carte détectée. Tentative d'anticollision...")
            (stat, raw_uid) = rdr.anticoll()
            if stat != rdr.OK:
                log_error("Échec de l'anticollision. Réessayez.")
                sleep(1)
                continue

            card_id = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            log_info(f"Carte lue avec succès: {card_id}")

            if card_id == "0x5a3dafb6":
                return True
            else:
                return False

        except Exception as e:
            log_error(f"Erreur inattendue: {e}")

        sleep(1)


