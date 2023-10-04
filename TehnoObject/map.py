from GameElement.decoration import Decoration


class Map:
    def __init__(self, mapObject):
        self.__mapObject = mapObject
        self.__decorations=[]

    def colision(self,player):
        for block in self.__decorations:
            block.colision(player)
    def integrate(self, scene, x, y):
        for pointY in range(len(self.__mapObject)):
            for pointX in range(len(self.__mapObject[pointY])):
                point=self.__mapObject[pointY][pointX]
                if(not point==0):
                    block=Decoration(pointX+x,pointY+y,point)
                    scene.addObject(block)
                    self.__decorations.append(block)