
class Parametr:
    def __init__(self,value):
        self.__value=value

    def get(self):
        return self.__value

    def set(self,value):
        self.__value=value

class ParametrAcamulate(Parametr):
    def set(self,value):
        super().set(value+self.get())

class Camera:
    def __init__(self,x:float,y:float):
        self.x:float=x
        self.y:float=y

class Scene:
    def __init__(self,camera,width,height):
        self.__map=[]
        self.__camera=camera
        self.__gameObjects=[]
        self.__width=width
        self.__height=height

    def initMap(self):
        self.__map=[(["."]*self.__width) for i in range(self.__height)]

    def addObject(self,object):
        self.__gameObjects.append(object)

    def removeObject(self,object):
        keyObject=None
        for i in range(len(self.__gameObjects)):
            if(self.__gameObjects[i]==object):
                keyObject=i
                break

        self.__gameObjects[keyObject],self.__gameObjects[-1]=self.__gameObjects[-1],self.__gameObjects[keyObject]
        self.__gameObjects.pop()

    def __drawObject(self,x,y,element):
        x=x-self.__camera.x
        y=y-self.__camera.y
        if(y<len(self.__map) and x<len(self.__map[0]) and x>=0 and y>=0):
            self.__map[y][x]=element

    def renderMap(self):
        self.initMap()

        for object in self.__gameObjects:
            self.__drawObject(object.x,object.y,object.element)

        for lineMap in self.__map:
            print("".join(lineMap))

    @property
    def map(self):
        return self.__map
class ObjectGame:
    def __init__(self,x:float,y:float,element:str):
        self.x:float=x
        self.y:float=y
        self.element:str=element


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


class Player(InteractiveObject):
    def __init__(self,x:float,y:float,element:str):
        super().__init__(x,y,input("імя гравця"),element,10,10,10)


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
class Cold(ObjectGame):
    def colision(self,player):
        if (self.x == player.x and self.y == player.y):
            print("end game")
            controler = input("пароль від сундука з золотом:").lower()
            if (controler == "прл"):
                print("Winner")
            else:
                print("Game Over")
            return "e"
        return ""

class Decoration(ObjectGame):
    def colision(self,player):
        preveCoords=player.preveCoords
        if(player.x==self.x and player.y==self.y):
            player.x=preveCoords["x"]
            player.y=preveCoords["y"]

class NPC(InteractiveObject):
    def __init__(self,x,y,name,element,live,atack,protect,riddle,model):
        super().__init__(x,y,name,element,live,atack,protect)
        self.__riddle=riddle
        self.__model=model

    def colision(self,player):
        if(self.x==player.x and self.y==player.y):
            return self.battle(player)
        return None

    def battle(self,player):
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
            return False
        if(self.live.get()<=0):
            player.live.set(10)
            player.atack.set(10)
            player.protect.set(10)
            return True



class Map:
    def __init__(self, mapObject):
        self.__mapObject = mapObject
        self.decorations=[]

    def integrate(self, scene, x, y):
        for pointY in range(len(self.__mapObject)):
            for pointX in range(len(self.__mapObject[pointY])):
                point=self.__mapObject[pointY][pointX]
                if(not point==0):
                    block=Decoration(pointX+x,pointY+y,point)
                    scene.addObject(block)
                    self.decorations.append(block)



camera=Camera(0,0)


scene=Scene(camera,10,10)
scene.initMap()

player=Player(3,3,"п")
scene.addObject(player)

cold=Cold(16,8,"з")
scene.addObject(cold)

nps=[]

nps1=NPC(3,2,"спіралеподібний","c",30,12,0,[["x^2-4=0;x1>0;x1=","2"],
                                                                             ["lim(x^2*5)=;x->0","0"],
                                                                             ["cos(0)=","1"],
                                                                             ["sin(pi/2)","1"],
                                                                             ["x/5=0","0"]],[[".",".",".","#",".",".",".","\n"],
                                                                                              [".",".","#","#","#",".",".","\n"],
                                                                                              [".","#","#","#","#","#",".","\n"],
                                                                                              [".","V","V","V","V","V",".","\n"],
                                                                                              [".","V","@","V","@","V",".","\n"],
                                                                                              [".","V","V","V","V","V",".","\n"],
                                                                                              [".","V","P","P","P","V",".","\n"],
                                                                                              [".",".","V","V","V",".",".","\n"]])
nps2=NPC(3,-8,"сфінкс","^",50,25,5,[["(x^5)'=","5x^4"],
                                                                             ["тіло рухається за законом s(t)=5t знайдіть закон швидкості","5"],
                                                                             ["x^2-5x+6=0 в відповідь запишіть суму коренів","5"],
                                                                             ["2^4x-5*2^2x+6 в відповідь запишіть раціональний корінь в вигляді десяткового дробу через кому","0.5"],
                                                                             ["sin(pi)","0"]],[[".","^","@","#","#","#","#","@","^","."]])
scene.addObject(nps1)
nps.append(nps1)
scene.addObject(nps2)
nps.append(nps2)

startMap=Map([["#","#","#","x","x","x","x","#","#","#"],
              ["#",0,0,0,0,0,0,0,0,"#"],
              ["#",0,0,0,0,0,0,0,0,"#"],
              ["#",0,0,0,0,0,0,0,0,"x"],
              ["#",0,0,"#","#","#","#",0,0,"x"],
              ["#", 0,0, "#", "#", "#", "#", 0, 0, "y"],
              ["#", 0, 0, 0, 0, 0, 0, 0, 0, "Q"],
              ["#",0,0,0,0,0,0,0,0,"#"],
              ["#",0,0,0,0,0,0,0,0,"#"],
              ["#","#","#","x",0,0,0,0,"x","x","#","#","#"],
              ["#","#","#",0,0,0,0,"#","#","#","#","#","#","x","d","d","d","#","#","#"],
              ["#",0,0,0,0,0,0,0,0,"#","#",0,0,0,0,0,0,0,0,"#"],
              ["#",0,0,0,0,0,0,0,0,"#","#",0,0,0,0,0,0,0,0,"#"],
              ["#",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"d"],
              ["#",0,0,"#","#","#","#",0,0,0,0,0,0,"#","#","#","#",0,0,0,"#"],
              ["#", 0,0, "#", "#", "#", "#", 0, 0, 0,0, 0,0, "#", "#", "#", "#", 0, 0, 0,"#"],
              ["#", 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"#"],
              ["#",0,0,0,0,0,0,0,0,"#","#",0,0,0,0,0,0,0,0,"#"],
              ["#",0,0,0,0,0,0,0,0,"#","#",0,0,0,0,0,0,0,0,"#"],
              ["#","#","#","x","#","x","x","#","#","#","#","#","#","x","#","x","x","#","#","#"]
])

startMap.integrate(scene,0,-10)

controler=""

print("w-move top")
print("s-move down")
print("a-move left")
print("d-move right")
print("і-інформація про персонажа")
print("п-{name}".format(name=player.name))
print("розшифруйте текст")
print("9-9(18)(15)(18)(22)(18)")
print("9(17)0(13)(22)(10) 9(18)(15)(18)(22)(18)")
print("алфавіт масив")
print("пароль від сундука з золотом-(19)(20)(15)")
print("щоб забрати 9 вам потрібно відповісти на питання охоронців c and ^")
level=0
while not controler=="e":
    player.move(controler)

    camera.x=player.x-5
    camera.y=player.y-5

    for block in startMap.decorations:
        block.colision(player)
    if(level==2):
        controler = cold.colision(player)
    for i in range(len(nps)):
        if(nps[i]):
            isNotGameOver=nps[i].colision(player)
            controler="e" if not isNotGameOver and not isNotGameOver==None else ""
            if(not controler and not isNotGameOver==None):
                scene.removeObject(nps[i])
                nps[i]=None
                level+=1

    scene.renderMap()

    print("if you want exit you need write e")
    if(not controler=="e"):
        controler=input("controler:").lower()


