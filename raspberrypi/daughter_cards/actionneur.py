#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.serialutils import Deserializer
from daughter_cards.arduino import SecureArduino, INT, BYTE, FLOAT
import time

# Instructions
RESET_OPCODE                = 0X12
PING_AX_OPCODE              = 0X13

SET_ID_OPCODE               = 0X14
SET_BD_OPCODE               = 0X15

MOVE_OPCODE                 = 0X16
MOVE_SPEED_OPCODE           = 0X17
TURN_OPCODE                 = 0x18

SET_ENDLESS_MODE_OPCODE     = 0X19
SET_TEMP_LIMIT_OPCODE       = 0X1A
SET_ANGLE_LIMIT_OPCODE      = 0X1B
SET_VOLTAGE_LIMIT_OPCODE    = 0X1C
SET_MAX_TORQUE_OPCODE       = 0X1D

READ_POSITION_OPCODE        = 0X1E
READ_SPEED_OPCODE           = 0X1F
READ_TORQUE_OPCODE          = 0X2A

"""
This class acts as an interface between the raspeberry pi and the arduino.
It contains methods relating to each action of the actuator.
It allows the raspeberry pi to ask the arduino to perform an action via a specific OPCODE.
"""
class Actionneur(SecureArduino):
    DEFAULT = {PING_AX_OPCODE: Deserializer(BYTE(0)), #idk
            }
    
    def __init__(self, parent, uuid='actionneurs'):
        SecureArduino.__init__(self, parent, uuid, self.DEFAULT)

class AX12(SecureArduino):
    DEFAULT = {PING_AX_OPCODE: Deserializer(BYTE(0)), 
            READ_POSITION_OPCODE: Deserializer(BYTE(0)), 
            READ_SPEED_OPCODE: Deserializer(BYTE(0)), 
            READ_TORQUE_OPCODE: Deserializer(BYTE(0)), 
            }
    def __init__(self, id, parent, uuid='actionneurs'):
        SecureArduino.__init__(self, parent, uuid, self.DEFAULT)
        self.id = id
    
    def reset(self): self.send(RESET_OPCODE, BYTE(self.id))

    def ping(self):
        output = self.execute(PING_AX_OPCODE, BYTE(self.id))
        return not bool(output.read(BYTE))

    def setID(self, newID): self.send(SET_ID_OPCODE, BYTE(self.id), BYTE(newID))

    def setBD(self, newBD): self.send(SET_BD_OPCODE, BYTE(self.id), INT(newBD))

    def move(self, Pos): self.send(MOVE_OPCODE, BYTE(self.id), FLOAT(Pos))

    def turn(self, Speed): self.send(TURN_OPCODE, BYTE(self.id), FLOAT(Speed))

    def stop_turn(self): self.turn(0)
    
    def moveSpeed(self, Pos, Speed): self.send(MOVE_SPEED_OPCODE, BYTE(self.id), FLOAT(Pos), FLOAT(Speed))

    def setEndlessMode(self, Status): self.send(SET_ENDLESS_MODE_OPCODE, BYTE(self.id), BYTE(Status))

    def setTempLimit(self, Temp): self.send(SET_TEMP_LIMIT_OPCODE, BYTE(self.id), BYTE(Temp))

    def setAngleLimit(self, CWLimit, CCWLimit): self.send(SET_ANGLE_LIMIT_OPCODE, BYTE(self.id), FLOAT(CWLimit), FLOAT(CCWLimit))

    def setVoltageLimit(self, DVoltage, UVoltage): self.send(SET_VOLTAGE_LIMIT_OPCODE, BYTE(self.id), BYTE(DVoltage), BYTE(UVoltage))

    def setMaxTorque(self, MaxTorque): self.send(SET_MAX_TORQUE_OPCODE, BYTE(self.id), INT(MaxTorque))

    def readPosition(self):
        output = self.execute(READ_POSITION_OPCODE, BYTE(self.id))
        return output.read(FLOAT)
    
    def readSpeed(self):
        output = self.execute(READ_SPEED_OPCODE, BYTE(self.id))
        return output.read(FLOAT)

    def readTorque(self):
        output = self.execute(READ_TORQUE_OPCODE, BYTE(self.id))
        return output.read(INT)


if __name__ == "__main__":
    from setups.setup_serialtalks import *

    s = Actionneur(manager)
    s.connect()

    ax = AX12(1)