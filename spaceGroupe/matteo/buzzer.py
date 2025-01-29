from machine import Pin, PWM
from time import sleep

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

# Initialisation du buzzer
BUZZER_PIN = 12
buzzer = PWM(Pin(BUZZER_PIN), freq=440, duty=0)

def jouer_note(note, duree):
    """
    Joue une note sur le buzzer.

    Args:
        note (str): La note à jouer (ex: "C", "D#", "R" pour silence).
        duree (float): La durée pendant laquelle jouer la note, en secondes.

    """
    if note in NOTES and NOTES[note] > 0:
        buzzer.freq(NOTES[note])
        buzzer.duty(20)  # Activer le buzzer (volume)
        sleep(duree)  # Jouer la note
        buzzer.duty(0)  # Arrêter le son
    else:
        sleep(duree)  # Silence

def sonnette():
    """
    Joue la mélodie de la sonnette prédéfinie.

    """
    for note, duree in MELODIE_SONNETTE:
        jouer_note(note, duree)
        sleep(0.1)  # Pause entre les notes

def rfid_bon():
    """
    Joue la mélodie indiquant une validation RFID réussie.

    """
    for note, duree in MELODIE_RFID_BON:
        jouer_note(note, duree)
        sleep(0.05)  # Pause courte entre les notes

def rfid_pasbon():
    """
    Joue la mélodie indiquant une validation RFID échouée.

    """
    for note, duree in MELODIE_RFID_PASBON:
        jouer_note(note, duree)
        sleep(0.05)  # Pause courte entre les notes