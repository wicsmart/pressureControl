from controller import Controller
import RPi.GPIO as GPIO
import Adafruit_ADS1x15
import smbus
import os
import time as time

class ControllerRaspi(Controller):

    adc=Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

    GPIO.setwarnings(False)
    GPIO.setmode (GPIO.BOARD)
    GPIO.setup (11, GPIO.OUT)       #Sinal Solenoide-Encher
    GPIO.setup (12, GPIO.OUT)       #sinal Solenoide-Esvaziar
    GPIO.setup (11, GPIO.HIGH)      #Rele inicialmente desligado
    GPIO.setup (12, GPIO.HIGH)      #Rele inicialmente desligado
    GPIO.setup (13, GPIO.OUT)       #Mux S0
    GPIO.setup (15, GPIO.OUT)       #Mux S1
    GPIO.setup (16, GPIO.OUT)       #Mux S2
    GPIO.setup (18, GPIO.OUT)       #Mux S3

    def __init__(self, limiteInferior, limiteSuperior, es):
        super(ControllerRaspi, self).__init__(limiteInferior, limiteSuperior, es)
  
    
    def limpaGPIO(self):
        GPIO.cleanup()
        
    def get_read_adc(self):
        return adc.read_adc(0, gain=self.GAIN)

    def enche_pneu(self):
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        GPIO.output(11, 1)
        GPIO.output(11, 0)
        time.sleep(0.5)
        GPIO.output(11, 1)

    def esvazia_pneu(self):
                
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(12, GPIO.OUT)
        GPIO.output(12, 1)
        GPIO.output(12, 0)
        time.sleep(0.5)
        GPIO.output(12, 1)