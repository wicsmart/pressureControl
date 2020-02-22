#-*- coding: utf-8 -*-
#!/usr/bin/python

from controllerSimulator import ControllerSimulator
import os
import time as time
from sender import elastic

if __name__ == "__main__":

    TOTAL_PNEUS = 6
    LIM_INFERIOR = 115
    LIM_SUPERIOR = 125
    PRESSAO_DESEJADA = 120

    # Cria sender
    sender = elastic("127.0.0.1","9220")
    
    if(sender.isConnected()):
        sender.create_empty_index()
    
    # Cria Controller
    controller = ControllerSimulator(LIM_INFERIOR, LIM_SUPERIOR, sender)
    
    pneu_atual = 0
    
    while( pneu_atual <= TOTAL_PNEUS ):

        controller.setPneu(pneu_atual)

        pressao = controller.getPressaoPneu()
        
        status = controller.getStatus(pressao)
                
        controller.sendMedida(pneu_atual, pressao, status)
       
        controller.atua(status)
        
        pneu_atual = pneu_atual + 1

        if(pneu_atual == TOTAL_PNEUS):
            pneu_atual = 0
            print("Todos os pneus estao OK!")
            controller.limpaGPIO()

        time.sleep(2)


