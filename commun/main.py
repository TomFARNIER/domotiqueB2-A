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




    # Initialisation des systèmes
    capteurMouvement.eteindre_led_rgb()
    buzzer.arreter()
    fenetre.fermer()
    porte.fermer()

    if not rfid_check():
        buzzer.on()
        buzzer.rfid_pasbon()
    else:
        buzzer.rfid_bon()
        loop = True

        while loop:
            if boutonStop.est_presse():
                loop = False


            if boutonOpen.est_presse():
                porte.ouvrir()
                fenetre.ouvrir()


            if detectPression.lire_valeur():
                buzzer.sonnette()

            if capteurMouvement.getValeurCapteur() == 1:
                capteurMouvement.mode_disco(5)

            if detecteurGaz.detecter_gaz():
                detecteurGaz.allumer_led()
                detecteurGaz.allumer_ventilo()
            else:
                detecteurGaz.eteindre_led()
                detecteurGaz.eteindre_ventilo()




if __name__ == "__main__":
    main()
