from daughter_cards.actionneur import Actionneur, AX12

class Pince:

    def __init__(self,manager):
        self.pince = AX12(3, manager, "actionneurs")
        self.pince.setEndlessMode(True)
        self.pince.setMaxTorque(1023)

    def fermer(self):
        self.pince.move(800)

    def ouvrir(self):
        #TODO
        return "TODO"

    def isFerme(self):
        return "TODO"
