# Système d'Automatisation Domestique

Ce script Python fait partie d'un système d'automatisation domestique qui intègre divers composants matériels tels que des boutons, des capteurs, des buzzeurs, des lecteurs RFID et des affichages. La fonctionnalité principale inclut la surveillance de l'état de ces composants et la réponse à des événements tels que des pressions de boutons ou des détections de capteurs.

## Vue d'Ensemble

Les principaux composants du système comprennent :

- **Bouton** : Représente les boutons pour les interactions utilisateur.
- **Buzzer** : Émet des alertes sonores.
- **CapteurMouvement** : Détecte le mouvement et contrôle les LED RGB.
- **Fenetre** : Représente une fenêtre qui peut être ouverte ou fermée.
- **GazController** : Gère la détection de gaz et la ventilation.
- **Porte** : Représente une porte qui peut être ouverte ou fermée.
- **DetectPression** : Détecte les niveaux de pression.
- **RFIDReader** : Lit les cartes RFID pour le contrôle d'accès.
- **LCDDisplay** : Affiche des informations et des alertes sur un écran LCD.

## Structure du Code

### Imports

```python
from teamCode import *
from time import sleep, time
from .librairy import DTHResult, DTH
from .librairy.mfrc5522 import MFRC522
from machine import Pin,ADC, PWM ,SPI
from random import randint
from neopixel import NeoPixel
from .dht import DTHResult
from .dht import DTH
from mfrc5522 import MFRC522


