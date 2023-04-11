#import imp
#from common.components import Manager
#from daughter_cards.wheeledbase import WheeledBase
#from daughter_cards.actionneur import Actionneur, AX12
#from tracking.libs.positionDetector import PositionDetector
#from daughter_cards.sensors import Sensors
#from setups.setup_serialtalks import *
#from listeners.sensor_listener import SensorListener
import time

from tracking.libs.positionDetectorMultiple import *
import math

posdetect=PositionDetectorMultiple()
posdetect.addMarkerId(17)
posdetect.init([0,0,0],math.radians(90),0)
print("init")
while True:
    posdetect.update()
    print(posdetect.markerPositions)


#pince=Pince(manager)

#pince.fermer()


#Connect to the Raspberry Pi and the different modules
<<<<<<< HEAD
#manager = Manager("10.0.0.5")
#manager.connect(7)

#actio = Actionneur(manager)
=======
manager = Manager("172.31.27.119")
manager.connect(7)

sensors = Sensors(manager, "sensors")
>>>>>>> 046d82180581c6b94e2080ca61e5f91181071413

print(sensors.is_ready())
print(sensors.check_errors())

<<<<<<< HEAD
#pince = AX12(3, manager) #AX12 avec l'ID 1
#pince.setMaxTorque(1023)
#pince.turn(-200)
=======
print(sensors.get_sensor1_range())
>>>>>>> 046d82180581c6b94e2080ca61e5f91181071413


<<<<<<< HEAD
#1 elevateur
#3 pince
#elevator = AX12(1, manager, "actionneurs")
#elevator.setEndlessMode(True)
#elevator.setMaxTorque(1023)
#elevator.turn(250)
#elevator.move(200)
#print("fin",elevator.ping())
#while True:
#    print(elevator.readPosition())
#for i in range(0,253):
    #elevator = AX12(i, manager, "actionneurs")
    #b=elevator.ping()
    
    #if b:
    #    print(i,b)
=======
>>>>>>> 046d82180581c6b94e2080ca61e5f91181071413
#LEFTCODEWHEEL_RADIUS_VALUE              = 21.90460280828869
#RIGHTCODEWHEEL_RADIUS_VALUE         = 22.017182927267537
#ODOMETRY_AXLETRACK_VALUE            = 357.5722465739272
# verifier les moteurs sans assver (vrif les sens de marche) open loop velocities
# verifier les codeuses et leur sens
# Faire la metrologie et l'enregistrer
# calibrer l'odométrie (verif la precision)
# calib asservisseement
