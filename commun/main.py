from teamCode import *

def main():
    # Initialisation des variables
    global loop

    # Initialisation des objets
    boutonStop = Bouton(5)
    boutonOpen = Bouton(14)
    buzzer = Buzzer(17)
    capteurMouvement = CapteurMouvement(14, 15, 10)
    fenetre = Fenetre(18)
    detecteurGaz = GazController(25, 16, 20)
    porte = Porte(27)
    detectPression = DetectPression(26)
    #rfid=RFIDReader(18,23,13,2,21,"0x5a3dafb6")
    lcd = LCDDisplay( 22, 21)




    # Initialisation des systèmes
    capteurMouvement.eteindre_led_rgb()
    buzzer.arreter()
    fenetre.fermer()
    porte.fermer()
    detecteurGaz.eteindre_led()
    detecteurGaz.eteindre_ventilo()
    porte.fermer()
    fenetre.fermer()

    """
    while True:
        buzzer.on()
        rfid_result = rfid.rfidCheck()  # Attendez que rfid_check() renvoie 1 ou 0
        if rfid_result == 1:
            lcd.afficher_rfid(True)
            buzzer.rfid_bon()
            loop = True
            sleep(1)
            break  # Sortez de la boucle si RFID est valide
        elif rfid_result == 0:
            lcd.afficher_rfid(False)
            buzzer.rfid_pasbon()
            sleep(1)
        else:
            sleep(1)
    """

    while loop:
        if boutonStop.est_presse():
            loop = False

        if boutonOpen.est_presse():
            lcd.afficher_trou(True,True)
            porte.ouvrir()
            fenetre.ouvrir()


        if detectPression.lire_valeur():
            buzzer.sonnette()

        if capteurMouvement.getValeurCapteur():
            capteurMouvement.mode_disco(5)


        if detecteurGaz.detecter_gaz():
            detecteurGaz.allumer_led()
            detecteurGaz.allumer_ventilo()
            lcd.afficher_gas()
            fenetre.fermer()
            lcd.afficher_trou(False,True)
        else:
            detecteurGaz.eteindre_led()
            detecteurGaz.eteindre_ventilo()
            lcd.clear()




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