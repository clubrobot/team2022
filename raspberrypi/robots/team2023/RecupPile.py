import math
import numpy as np
from time import sleep
class RecupPile:

    def __init__(self,wheeledbase,positionPoint,endPoint,pince,ascen) -> None:
        self.wb=wheeledbase
        self.pos=np.array(positionPoint)
        self.radiusRobot=400
        self.radiusPince=230
        self.pince=pince
        self.asc=ascen
        self.actionpoint=None
        self.orientation=None
        self.endPoint=np.array(endPoint)
        pass

    def procedure(self, robot):
        #self.wb.goto_stop(self.pos[0],self.pos[1],robot.sensors,theta=ang)
        #print(self.wb.get_position(),self.pos)
        #sleep(20)
        print("1"),self.asc
        #self.asc.rouler()
        print("2")
        rPos=np.array(self.wb.get_position()[:2])
        #print(self.pos,rPos)
        vecPos=self.pos-rPos[:2]
        length=math.sqrt(vecPos[0]**2+vecPos[1]**2)
        stop=vecPos/length*(length-self.radiusRobot)+rPos
        ang=math.acos(vecPos[0]/length)
        if(vecPos[1]<0):
            ang*=-1
        #print("p1",stop,self.wb.get_position(),length)
        #print(self.pos)
        if(length-self.radiusRobot>0):
            self.wb.goto_stop(stop[0],stop[1],robot.sensors,theta=ang)
            print(self.wb.get_position(),stop)
        self.pince.ouvrir()
        #self.asc.bas()
        stop=vecPos/length*(length-self.radiusPince)+rPos
        self.wb.goto_stop(stop[0],stop[1],robot.sensors,theta=ang)
        print(self.wb.get_position(),stop)
        sleep(2)
        self.pince.fermer()
        #self.asc.rouler()

        #va poser à la fin
        rPos=np.array(self.wb.get_position()[:2])
        vecPos=self.endPoint-rPos
        length=math.sqrt(vecPos[0]**2+vecPos[1]**2)
        stop=vecPos/length*(length-self.radiusPince)+rPos
        ang=math.acos(vecPos[0]/length)
        if(vecPos[1]<0):
            ang*=-1
        #print("p3",self.endPoint,ang)
        self.wb.goto_stop(stop[0],stop[1],robot.sensors,theta=ang)
        print(self.wb.get_position(),stop)
        sleep(4)
        #self.asc.bas()
        self.pince.ouvrir()

        self.wb.set_openloop_velocities(-500,-500)
        sleep(0.3)
        self.wb.stop()
        #self.asc.rouler()