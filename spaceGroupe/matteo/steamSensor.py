import machine
import time

PIN_ANALOG_STEAM_SENSOR_IN = 34  # Select PIN

# Initialisation de l'ADC en dehors de la fonction pour éviter une recréation inutile
adc = machine.ADC(machine.Pin(PIN_ANALOG_STEAM_SENSOR_IN))
adc.atten(machine.ADC.ATTN_11DB)  # Plage de 0 à 3.3V pour ESP32


def steamSensor():
    """Permet de lire la valeur du capteur de pression

    Returns:
            True(bool) : si la valeur est supérieure à 40
            False(bool) : si la valeur est inférieure à 40
    """

    adc_val = adc.read()
    dac_val = round(adc_val * 255 / 4095)
    print(f"ADC Val: {adc_val}, \t DAC Val: {dac_val}")

    if dac_val >= 40:
        #APPELER LA FONCTION SONNETTE (sonnette()) qui est dans buzzer.py
        return True
    else:
        return False


