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
manager = Manager("10.0.0.3")
manager.connect(10)

from setups.setup_serialtalks import *

btn1 = LightButton(gpio_pins.INTER_1_PIN, gpio_pins.LED1_PIN, print("BTN1"));
btn2 = LightButton(gpio_pins.INTER_2_PIN, gpio_pins.LED2_PIN, print("BTN2"));
btn3 = LightButton(gpio_pins.INTER_3_PIN, gpio_pins.LED3_PIN, print("BTN3"));
btn4 = LightButton(gpio_pins.INTER_4_PIN, gpio_pins.LED4_PIN, print("BTN4"));

btn1.on()
btn2.on()
btn3.on()
btn4.on()

tirette = Switch(gpio_pins.TIRETTE_PIN, print("tirette"))

#	print(wb.get_position())
#	ac.set_clamp_position(1,180)
#	print(sensors.get_sensor3_range())
#	print(sensors.get_all())
	
#LEFTCODEWHEEL_RADIUS_VALUE              = 21.90460280828869
#RIGHTCODEWHEEL_RADIUS_VALUE         = 22.017182927267537
#ODOMETRY_AXLETRACK_VALUE            = 357.5722465739272
# verifier les moteurs sans assver (vrif les sens de marche) open loop velocities
# verifier les codeuses et leur sens
# Faire la metrologie et l'enregistrer
# calibrer l'odométrie (verif la precision)
# calib asservisseement
