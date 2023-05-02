from common.components import Manager
#from daughter_cards.wheeledbase import WheeledBase
#from daughter_cards.actionneur import Actionneur, AX12
#from tracking.libs.positionDetector import PositionDetector
#from daughter_cards.sensors import Sensors
import time
#from tracking.libs.positionDetectorMultiple import *
import math
#from common.gpiodevices import Switch, LightButton, gpio_pins
manager = Manager("10.0.0.3")

manager.connect(7)

from setups.setup_serialtalks import *

from managers.buttons_manager import ButtonsManager
ButtonsManager(None).begin()

#LEFTCODEWHEEL_RADIUS_VALUE              = 21.90460280828869
#RIGHTCODEWHEEL_RADIUS_VALUE         = 22.017182927267537
#ODOMETRY_AXLETRACK_VALUE            = 357.5722465739272
# verifier les moteurs sans assver (vrif les sens de marche) open loop velocities
# verifier les codeuses et leur sens
# Faire la metrologie et l'enregistrer
# calibrer l'odométrie (verif la precision)
# calib asservisseement
