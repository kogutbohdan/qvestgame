from TehnoObject.arrayFunctions import removeElementInArray


class NPCColection:
    def __init__(self,scene):
        self.__nps=[]
        self.__scene=scene


    def add(self,nps):
        self.__nps.append(nps)
        self.__scene.addObject(nps)

    def remove(self,nps):
        removeElementInArray(self.__nps,nps)
        self.__scene.removeObject(nps)

    def colision(self,player,controler,preveLevel):
        for nps in self.__nps:
            nps.colision(player,controler)
            if(not controler.value=="e" and not player.level.get()==preveLevel):
                self.remove(nps)
