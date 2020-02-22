
#-*- coding: utf-8 -*-
#!/usr/bin/python
import os
import time as time
import random as random
import datetime


class Controller(object):
    
    os.environ["TZ"] = "America/Sao_Paulo"
    GAIN = 1
    value = [0]

    def __init__(self, limiteInferior, limiteSuperior, es):
        self.lim_inferior = limiteInferior
        self.lim_superior = limiteSuperior
        self.es = es

    def setS0(self, sinal):
        pass

    def setS1(self, sinal):
        pass

    def setS2(self, sinal):
        pass

    def setS3(self, sinal):
        pass
    
    def limpaGPIO(self):
        pass

# Defini qual pneu o sensor irá ler os dados
    def setPneu(self, pneu):
        print("lendo pneu "+ str(pneu))
        if (pneu == 0):
            self.setS0(0)
            self.setS1(0)
            self.setS2(0)
            self.setS3(0)
        if (pneu == 1):
            self.setS0(1)
            self.setS1(0)
            self.setS2(0)
            self.setS3(0)
        if (pneu == 2):
            self.setS0(0)
            self.setS1(1)
            self.setS2(0)
            self.setS3(0)
        if (pneu == 3):
            self.setS0(1)
            self.setS1(1)
            self.setS2(0)
            self.setS3(0)
        if (pneu == 4):
            self.setS0(0)
            self.setS1(0)
            self.setS2(1)
            self.setS3(0)
        if (pneu == 5):
            self.setS0(1)
            self.setS1(0)
            self.setS2(1)
            self.setS3(0)
        if (pneu == 6):
            self.setS0(0)
            self.setS1(1)
            self.setS2(1)
            self.setS3(0)
        if (pneu == 7):
            self.setS0(1)
            self.setS1(1)
            self.setS2(1)
            self.setS3(0)
        if (pneu == 8):
            self.setS0(0)
            self.setS1(0)
            self.setS2(0)
            self.setS3(1)
        if (pneu == 9):
            self.setS0(1)
            self.setS1(0)
            self.setS2(0)
            self.setS3(1)
        if (pneu == 10):
            self.setS0(0)
            self.setS1(1)
            self.setS2(0)
            self.setS3(1)
        if (pneu == 11):
            self.setS0(1)
            self.setS1(1)
            self.setS2(0)
            self.setS3(1)
        if (pneu == 12):
            self.setS0(0)
            self.setS1(0)
            self.setS2(1)
            self.setS3(1)
        if (pneu == 13):
            self.setS0(1)
            self.setS1(0)
            self.setS2(1)
            self.setS3(1)
        if (pneu == 14):
            self.setS0(0)
            self.setS1(1)
            self.setS2(1)
            self.setS3(1)
        if (pneu == 15):
            self.setS0(1)
            self.setS1(1)
            self.setS2(1)
            self.setS3(1)           

# Lê sensor. Obs: o sensor deve ser setado para um pneu specifico pela funcao setPneu
    def getPressaoPneu(self):
        self.value[0] = self.get_read_adc()
        volts = self.value[0] / 32767.0 * 4.096
        psi = 50 * volts - 25
        return psi
    
# Verifica se a pressão está ok
    def getStatus(self, psi):
        if(psi < self.lim_inferior):
            return 'Vazio'
        
        if(psi > self.lim_superior):
            return 'Cheio'

        return 'Ok'
        
# Envia dados para o elasticsearch
    def sendMedida(self, pneu, psi, status):
        data_hora = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        doc = {
            "psi" : psi,
            "pneu" : pneu,
            "status": status,
            "data_hora" : data_hora
        }
        if self.es.isConnected():
            self.es.store_record(doc)


# Verifica se precisa encher ou esvaziar e atua
    def atua(self, status):
        if(status == "Vazio"):
            while self.getPressaoPneu() < self.lim_inferior:
                self.enche_pneu()

        elif(status == "Cheio"):
            while self.getPressaoPneu() > self.lim_superior:
                self.esvazia_pneu() 
            


    def get_read_adc(self):
        pass

    def enche_pneu(self):
        pass

    def esvazia_pneu(self):
        pass