from GameElement.interactiveObject import InteractiveObject
from TehnoObject.parametr import ParametrAcamulate


class Player(InteractiveObject):
    def __init__(self,x:float,y:float,element:str):
        super().__init__(x,y,input("імя гравця"),element,10,10,10)
        self.level=ParametrAcamulate(0)


    def move(self,controler):
        self.__preveX=self.x
        self.__preveY = self.y
        if (controler == "w"):
            self.y -= 1
        elif (controler == "s"):
            self.y += 1
        elif (controler == "a"):
            self.x -= 1
        elif (controler == "d"):
            self.x += 1
        elif (controler=="i"):
            self.printInfo()


    @property
    def preveCoords(self):
        return {
            "x":self.__preveX,
            "y":self.__preveY
        }