from daughter_cards.actionneur import Actionneur, AX12

class Ascenseur:

    def __init__(self,manager):
        self.asc = AX12(1, manager, "actionneurs")
        self.asc.setEndlessMode(True)
        self.asc.setMaxTorque(1023)
        self.v_bas=0

#300 haut de la pince bas du magasin
    def bas(self):
        #print(self.asc.readPosition())
        self.asc.move(self.v_bas)
        
            
        #self.asc.move(-500)