from teamCode import *

def main():
    # Initialisation des variables
    global loop

    # Initialisation des objets
    boutonStop = Bouton(12)
    boutonOpen = Bouton(13)
    buzzer = Buzzer(21)
    capteurMouvement = CapteurMouvement(14, 15, 10)
    fenetre = Fenetre(16)
    detecteurGaz = GazController(18, 19, 20)
    porte = Porte(17)
    detectPression = DetectPression(22)
    rfid=RFIDReader(18,23,19,2,21,"0x5a3dafb6")




    # Initialisation des systèmes
    capteurMouvement.eteindre_led_rgb()
    buzzer.arreter()
    fenetre.fermer()
    porte.fermer()
    detecteurGaz.eteindre_led()
    detecteurGaz.eteindre_ventilo()
    porte.fermer()
    fenetre.fermer()

    while True:
        rfid_result = rfid.rfidCheck()  # Attendez que rfid_check() renvoie 1 ou 0
        if rfid_result == 1:
            buzzer.rfid_bon()
            loop = True
            sleep(1)
            break  # Sortez de la boucle si RFID est valide
        elif rfid_result == 0:
            buzzer.on()
            buzzer.rfid_pasbon()
            sleep(1)
        else:
            sleep(1)

    while loop:
        if boutonStop.est_presse():
            loop = False

        if boutonOpen.est_presse():
            porte.ouvrir()
            fenetre.ouvrir()


        if detectPression.lire_valeur():
            buzzer.sonnette()

        if capteurMouvement.getValeurCapteur():
            capteurMouvement.mode_disco(5)

        if detecteurGaz.detecter_gaz():
            detecteurGaz.allumer_led()
            detecteurGaz.allumer_ventilo()
        else:
            detecteurGaz.eteindre_led()
            detecteurGaz.eteindre_ventilo()




if __name__ == "__main__":
    try:
        while True:
            main()
            sleep(1)
            if is_pressed('q'):
                print("Program terminated gracefully by pressing 'q'.")
                break
    except KeyboardInterrupt:
        print("Program terminated by user.")