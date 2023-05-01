import math

class RecupPile:

    def __init__(self,wheeledbase,positionPoint,endPoint,pince) -> None:
        self.wb=wheeledbase
        self.pos=positionPoint
        self.radiusRobot=100
        self.radiusPince=50
        self.pince=pince
        self.actionpoint=None
        self.orientation=None
        self.endPoint=endPoint
        pass

    def procedure(self, robot):
        rPos=self.wb.getPosition()
        vecPos=self.pos-rPos
        length=math.sqrt(vecPos[0]**2+vecPos[1]**2)
        stop=vecPos/length*(length-self.radiusRobot)
        ang=math.acos(vecPos[0]/length)
        if(vecPos[1]<0):
            ang*=-1
        self.wb.goto_stop(stop[0],stop[1],robot.sensors,theta=ang)
        self.pince.ouvrir()
        stop=vecPos/length*(length-self.radiusPince)
        self.wb.goto_stop(self.pos[0],self.pos[1],robot.sensors,theta=ang)
        self.pince.fermer()

        #va poser à la fin
        rPos=self.wb.getPosition()
        vecPos=self.endPoint-rPos
        length=math.sqrt(vecPos[0]**2+vecPos[1]**2)
        stop=vecPos/length*(length-self.radiusPince)
        ang=math.acos(vecPos[0]/length)
        if(vecPos[1]<0):
            ang*=-1
        self.wb.goto_stop(self.pos[0],self.pos[1],robot.sensors,theta=ang)
        self.pince.ouvrir()