#import imp
from common.components import Manager
from common.gpiodevices import Switch, LightButton, gpio_pins
from daughter_cards.wheeledbase import WheeledBase
from daughter_cards.actionneur import Actionneur
from daughter_cards.display import LEDMatrix, SevenSegments
from tracking.libs.positionDetector import PositionDetector
from daughter_cards.sensors import Sensors
from listeners.sensor_listener import SensorListener



# Connect to the Raspberry Pi and the different modules
manager = Manager("10.0.0.2")
manager.connect(10)

from setups.setup_serialtalks import *

s = Actionneur(manager)
s.connect()

ax = s.AX12(1, s)
ax2 = s.AX12(3, s)

ax2.move(200)
ax.move(100)

	
#LEFTCODEWHEEL_RADIUS_VALUE              = 21.90460280828869
#RIGHTCODEWHEEL_RADIUS_VALUE         = 22.017182927267537
#ODOMETRY_AXLETRACK_VALUE            = 357.5722465739272
# verifier les moteurs sans assver (vrif les sens de marche) open loop velocities
# verifier les codeuses et leur sens
# Faire la metrologie et l'enregistrer
# calibrer l'odométrie (verif la precision)
# calib asservisseement
