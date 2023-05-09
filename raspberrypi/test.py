from common.components import Manager
from daughter_cards.wheeledbase import WheeledBase
#from daughter_cards.actionneur import Actionneur, AX12
#from tracking.libs.positionDetector import PositionDetector
#from daughter_cards.sensors import Sensors
import time
#from tracking.libs.positionDetectorMultiple import *
import math
from robots.team2023.team2023Robot import Bornibus
#from common.gpiodevices import Switch, LightButton, gpio_pins
manager = Manager("10.0.0.3")

manager.connect(7)

from setups.setup_serialtalks import *

born=Bornibus(manager=manager)
born.start()

"""wb=WheeledBase(manager)
print(wb.left_wheel_radius.get())
print(wb.right_wheel_radius.get())
ratio=wb.left_codewheel_radius.get()/wb.right_codewheel_radius.get()
radius=wb.right_codewheel_radius.get()
radius=23
ratio=1.0
print(wb.wheels_axletrack.get())
wb.wheels_axletrack.set(100)
wb.right_codewheel_radius.set(radius)
wb.left_codewheel_radius.set(ratio*radius)
print(ratio)

wb.set_position(0,0,0)
#wb.set_openloop_velocities(500,0)
wb.goto(0,500,finalangle=1.57)
#wb.turnonthespot(3.14)
wb.save_parameters()
while True:
    True
    #print(wb.get_position())
print("arrivé")"""

#from managers.buttons_manager import ButtonsManager
#ButtonsManager(None).begin()

#LEFTCODEWHEEL_RADIUS_VALUE              = 21.90460280828869
#RIGHTCODEWHEEL_RADIUS_VALUE         = 22.017182927267537
#ODOMETRY_AXLETRACK_VALUE            = 357.5722465739272
# verifier les moteurs sans assver (vrif les sens de marche) open loop velocities
# verifier les codeuses et leur sens
# Faire la metrologie et l'enregistrer
# calibrer l'odométrie (verif la precision)
# calib asservisseement
