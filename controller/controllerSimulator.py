from controller import Controller
import os
import time as time
import random as random

class ControllerSimulator(Controller):

    PRESSAO_DESEJADA = 120

    def __init__(self, limiteInferior, limiteSuperior, es):
        super(ControllerSimulator, self).__init__(limiteInferior, limiteSuperior, es)
    

    def get_read_adc(self):
        return random.randint(17000,28000)

    def enche_pneu(self):
        return self.PRESSAO_DESEJADA + 2
    
    def esvazia_pneu(self):
        return self.PRESSAO_DESEJADA - 2