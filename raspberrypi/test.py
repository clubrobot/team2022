#import imp
from common.components import Manager
from daughter_cards.wheeledbase import WheeledBase
from daughter_cards.actionneur import Actionneur, AX12
from tracking.libs.positionDetector import PositionDetector
from daughter_cards.sensors import Sensors
from setups.setup_serialtalks import *
from listeners.sensor_listener import SensorListener




# Connect to the Raspberry Pi and the different modules
manager = Manager("10.0.0.11")
manager.connect(7)

actio = Actionneur(manager, "actionneurs")

elevator = AX12(1); #AX12 avec l'ID 1


# Connect wheeledbase

wb = WheeledBase(manager)

#sensors =Sensors(manager, "sensors")


# '/dev/tty.SLAB_USBtoUART'
# sensors.last_time
#print(sensors.is_ready())
#print(sensors.check_errors())


def passe():
	return 0,0

print(wb.get_position())
print(wb.left_codewheel_counts_per_rev.get())
print(wb.right_codewheel_counts_per_rev.get())
#while(True):
wb.turnonthespot(3.14)
	#print(sensors.get_sensor1_range())
print(wb.get_position())
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
