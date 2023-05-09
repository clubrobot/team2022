from common.components import Manager
from daughter_cards.wheeledbase import WheeledBase
from robots.team2023.ascenseur import Ascenseur
from robots.team2023.pince import Pince
from daughter_cards.sensors import Sensors
from threading import Thread
from common.geogebra import Geogebra
from common.roadmap import RoadMap
from robots.team2023.RecupPile import RecupPile
import os
import math

class Robot:
    def __init__(self,manager,side) -> None:
        for root, dirs, files in os.walk("."):
            for file in files:
                if file == "map_2023.ggb":
                    roadmap_path = os.path.join(root, file)
        
        self.geo  = Geogebra(roadmap_path)#"robots/team2023/map_2023.ggb"
        self.road = RoadMap.load(self.geo)
        self.side = side

        self.wheeledbase = WheeledBase(manager)
        #self.display = display
        self.pince= Pince(manager)
        self.ascenseur= Ascenseur(manager)
        #self.sensors=Sensors(manager,"sensors")
        self.sensors=None
        self.blue=self.side=="BLUE"

        h=100
        v=300


        self.automate = []#get 3 couleurs puis gerber puis poser cerises
        if(self.blue):#couleur impaire
            born.wheeledbase.set_position(3000-h/2,v/2,-math.pi/2)
            self.base=self.geo.get('ZB1')
            self.end=self.geo.get('ZB2')
            self.automate.append(RecupPile(self.wheeledbase,self.geo.get('Rose1'),self.geo.get('ZB1'),self.pince))
            self.automate.append(RecupPile(self.wheeledbase,self.geo.get('Noir1'),self.geo.get('ZB1'),self.pince))
            self.automate.append(RecupPile(self.wheeledbase,self.geo.get('Jaune1'),self.geo.get('ZB1'),self.pince))
        else:#couleur paire
            self.base=self.geo.get('ZV1')
            self.end=self.geo.get('ZV2')
            born.wheeledbase.set_position(3000-h/2,2000-v/2,-math.pi/2)
            self.automate.append(RecupPile(self.wheeledbase,self.geo.get('Rose2'),self.geo.get('ZV1'),self.pince))
            self.automate.append(RecupPile(self.wheeledbase,self.geo.get('Noir2'),self.geo.get('ZV1'),self.pince))
            self.automate.append(RecupPile(self.wheeledbase,self.geo.get('Jaune2'),self.geo.get('ZV1'),self.pince))


    def start(self):
        self.wheeledbase.goto_sensors(self.centre[0],self.centre[1],sensors=self.sensors)
        #attend tirette
        print("A")
        self.automate[0].procedure(self)
        self.automate[1].procedure(self)
        print("cc")
        self.wheeledbase.goto_sensors(self.end[0],self.end[1],sensors=self.sensors)
    


from common.components import Manager
manager = Manager("10.0.0.3")

manager.connect(7)

from setups.setup_serialtalks import *

born=Robot(manager=manager,side="BLUE")

print("cree")
born.start()