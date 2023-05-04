from common.components import Manager
from daughter_cards.wheeledbase import WheeledBase
from daughter_cards.actionneur import Actionneur
from daughter_cards.display import LEDMatrix, SevenSegments
from tracking.libs.positionDetector import PositionDetector
from daughter_cards.sensors import Sensors
from listeners.sensor_listener import SensorListener
from time import sleep



# Connect to the Raspberry Pi and the different modules
manager = Manager("10.0.0.3")
manager.connect(10)

from setups.setup_serialtalks import *

sen = Sensors(manager, "sensors")
print(sen.subscribeSensors())
print(sen.unsubscribeSensors())