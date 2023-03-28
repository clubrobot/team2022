#import imp
from common.components import Manager
from daughter_cards.wheeledbase import WheeledBase
from daughter_cards.actionneur import Actionneur, AX12
from tracking.libs.positionDetector import PositionDetector
from daughter_cards.sensors import Sensors
from setups.setup_serialtalks import *
from listeners.sensor_listener import SensorListener
import time



#Connect to the Raspberry Pi and the different modules
manager = Manager("10.0.0.11")
manager.connect(7)

actio = Actionneur(manager)

#for i in range(0,20):
#	elevator = AX12(i, manager, "actionneurs"); #AX12 avec l'ID 1
#	print(i)
#	print(elevator.ping())

pince = AX12(3, manager) #AX12 avec l'ID 1
pince.setMaxTorque(1023)
#pince.turn(-200)

#time.sleep(10)

elevator = AX12(1, manager, "actionneurs")
elevator.setEndlessMode(True)
elevator.setMaxTorque(1023)
elevator.turn(500)
#LEFTCODEWHEEL_RADIUS_VALUE              = 21.90460280828869
#RIGHTCODEWHEEL_RADIUS_VALUE         = 22.017182927267537
#ODOMETRY_AXLETRACK_VALUE            = 357.5722465739272
# verifier les moteurs sans assver (vrif les sens de marche) open loop velocities
# verifier les codeuses et leur sens
# Faire la metrologie et l'enregistrer
# calibrer l'odométrie (verif la precision)
# calib asservisseement
