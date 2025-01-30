from idlelib.pyparse import trans

from __libs__ import Pin, PWM, sleep

# Définition des fréquences des notes en Hz
NOTES = {
    "A": 440, "B": 494, "C": 523, "D": 587, "E": 659, "F": 698, "G": 784,
    "A#": 466, "C#": 554, "D#": 622, "F#": 740, "G#": 831,
    "R": 0  # Silence
}

# Mélodies (Notes et durées en secondes)
MELODIE_SONNETTE = [
    ("E", 0.4), ("F#", 0.4), ("A", 0.4), ("B", 0.4),
    ("A", 0.4), ("F#", 0.4), ("E", 0.4), ("D", 0.4),
    ("E", 0.8), ("R", 0.2),  # Pause
    ("E", 0.4), ("F#", 0.4), ("A", 0.4), ("B", 0.4),
    ("A", 0.4), ("F#", 0.4), ("E", 0.4), ("D", 0.4),
    ("E", 0.8)
]

MELODIE_RFID_BON = [
    ("C", 0.1), ("E", 0.1), ("G", 0.1), ("C", 0.3),
    ("E", 0.1), ("G", 0.1), ("B", 0.1), ("E", 0.3),
    ("G", 0.1), ("B", 0.1), ("D", 0.1), ("G", 0.3),
    ("B", 0.1), ("D", 0.1), ("F", 0.1), ("B", 0.3),
    ("D", 0.1), ("F", 0.1), ("A", 0.1), ("D", 0.5)
]

MELODIE_RFID_PASBON = [
    ("E", 0.2), ("C", 0.2), ("A", 0.2), ("R", 0.1),
    ("G", 0.2), ("E", 0.2), ("C", 0.5)
]

class Buzzer:
    """
    Classe pour contrôler un buzzer via PWM.

    Attributes:
        buzzer (PWM): Instance du buzzer configurée avec PWM.
    """

    def __init__(self, buzzer_pin : int):
        """
        Initialise et configure le buzzer avec PWM.

        Args:
            buzzer_pin (int): Le numéro du pin auquel le buzzer est connecté.
        """
        self.buzzer = PWM(Pin(buzzer_pin), freq=440, duty=0)

    def jouer_note(self, note , duree : float):
        """
        Joue une note sur le buzzer.

        Args:
            note (str): La note à jouer (ex: "C", "D#", "R" pour silence).
            duree (float): La durée pendant laquelle jouer la note, en secondes.
        """
        if note in NOTES and NOTES[note] > 0:
            self.buzzer.freq(NOTES[note])
            self.buzzer.duty(20)  # Activer le buzzer (volume)
            sleep(duree)  # Jouer la note
            self.buzzer.duty(0)  # Arrêter le son
        else:
            sleep(duree)  # Silence

        return None

    def sonnette(self):
        """
        Joue la mélodie de la sonnette prédéfinie.
        """
        for note, duree in MELODIE_SONNETTE:
            self.jouer_note(note, duree)
            sleep(0.1)  # Pause entre les notes
        sleep(1)
        return None

    def rfid_bon(self):
        """
        Joue la mélodie indiquant une validation RFID réussie.
        """
        for note, duree in MELODIE_RFID_BON:
            self.jouer_note(note, duree)
            sleep(0.05)  # Pause courte entre les notes
        sleep(1)

        return None

    def rfid_pasbon(self):
        """
        Joue la mélodie indiquant une validation RFID échouée.
        """
        for note, duree in MELODIE_RFID_PASBON:
            self.jouer_note(note, duree)
            sleep(0.05)  # Pause courte entre les notes
        sleep(1)
        return None

    def arreter(self):
        """
        Arrête le buzzer.
        """
        self.buzzer.duty(0)
        sleep(1)
        return None

    def on(self):
        """
        Allume le buzzer.
        """
        self.buzzer.duty(20)
        return None
