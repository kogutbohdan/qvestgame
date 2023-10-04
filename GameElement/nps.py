from GameElement.interactiveObject import InteractiveObject


class NPC(InteractiveObject):
    def __init__(self,x,y,name,element,live,atack,protect,riddle,model):
        super().__init__(x,y,name,element,live,atack,protect)
        self.__riddle=riddle
        self.__model=model

    def colision(self,player,controler):
        if(self.x==player.x and self.y==player.y):
            return self.battle(player,controler)
        return None

    def battle(self,player,controler):
        i=0
        while player.live.get()>0 and self.live.get()>0 and i<len(self.__riddle):
            for lineModel in self.__model:
                print("".join(lineModel))
            print("{name} життя {live}.................{nameNPC} життя {liveNPC}".format(name=player.name,live=player.live.get(),nameNPC=self.name,liveNPC=self.live.get()))
            print("загадка:\n"+self.__riddle[i][0])
            result=input("відповідь на загадку:").lower()
            if(result==self.__riddle[i][1]):
                self.live.set(-(player.atack.get()-self.protect.get()))
            else:
                player.live.set(-(self.atack.get()-player.protect.get()))
            i+=1
        if(player.live.get()<=0 or (i>=len(self.__riddle) and self.live.get()>0)):
            print("game over")
            controler.value="e"
        if(self.live.get()<=0):
            print("ви перемогли охоронця")
            player.live.set(10)
            player.atack.set(10)
            player.protect.set(10)
            player.level.set(1)