from teamCode import *

def main():
    global loop
    sleep(10)

    # Initialisation des objets
    boutonStop = Bouton(12)
    boutonOpen = Bouton(13)
    buzzer = Buzzer(21)
    capteurMouvement = CapteurMouvement(14, 15, 10)
    fenetre = Fenetre(16)
    detecteurGaz = GazController(18, 19, 20)
    porte = Porte(17)
    detectPression = DetectPression(22)




    # Initialisation des systèmes
    capteurMouvement.eteindre_led_rgb()
    buzzer.arreter()
    fenetre.fermer()
    porte.fermer()

    if not rfid_check():
        buzzer.on()
        sleep(3)
        buzzer.rfid_pasbon()
    else:
        buzzer.rfid_bon()
        loop = True

        while loop:
            if boutonStop.est_presse():
                loop = False
                sleep(1)

            if boutonOpen.est_presse():
                porte.ouvrir()
                fenetre.ouvrir()
                sleep(1)

            if detectPression.lire_valeur():
                buzzer.sonnette()
                sleep(1)

            if capteurMouvement.getValeurCapteur() == 1:
                capteurMouvement.mode_discot(5)

            if detecteurGaz.detecter_gaz() == 1:
                detecteurGaz.allumer_led()
                detecteurGaz.allumer_ventilo()
            else:
                detecteurGaz.eteindre_led()
                detecteurGaz.eteindre_ventilo()




if __name__ == "__main__":
    main()
