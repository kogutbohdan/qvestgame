from GameElement.objectGame import ObjectGame
from TehnoObject.parametr import ParametrAcamulate


class InteractiveObject(ObjectGame):
    def __init__(self,x,y,name,element,live,atack,protect):
        super().__init__(x,y,element)
        self.__name=name
        self.live=ParametrAcamulate(live)
        self.atack=ParametrAcamulate(atack)
        self.protect=ParametrAcamulate(protect)

    def printInfo(self):
        live=self.live.get()
        protect=self.protect.get()
        atack=self.atack.get()
        print(f"імя {self.name}")
        print(f"кількість життя {live}")
        print(f"захист {protect}")
        print(f"напад {atack}")
    @property
    def name(self):
        return self.__name