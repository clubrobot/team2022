from daughter_cards.actionneur import Actionneur
import time
class Ascenseur:

    def __init__(self,manager):
        self.asc = manager.AX12(3, manager)
        self.asc.setEndlessMode(True)
        self.asc.setMaxTorque(1023)
        self.v_bas=100

    def rouler(self):
        end=450
        self.asc.move(end)
        deb=time.time()
        self.asc.readPosition()
        while((abs(self.asc.readPosition()-end)>5 )and time.time()-deb<3):
            
            #print(abs(self.asc.readPosition()-end),self.asc.readSpeed())
            continue

#300 haut de la pince bas du magasin
    def bas(self):
        end=self.v_bas
        self.asc.move(100)
        deb=time.time()
        self.asc.readPosition()
        while((abs(self.asc.readPosition()-end)>5 or self.asc.readSpeed()>0)and time.time()-deb<3):
  
            
            #print(self.asc.readPosition(),self.asc.readTorque())
            continue
        
            
        #self.asc.move(-500)