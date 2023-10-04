from GameElement.cold import Cold
from GameElement.nps import NPC
from GameElement.player import Player
from TehnoObject.controller import*
from TehnoObject.map import Map
from TehnoObject.npscolection import*
from TehnoObject.camera import*
from TehnoObject.scene import*

camera=Camera(0,0)


scene=Scene(camera,20,10)
scene.initMap()

player=Player(3,3,"п")
scene.addObject(player)

cold=Cold(16,8,"з")
scene.addObject(cold)

nps=NPCColection(scene)

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
nps2=NPC(3,-8,"сфінкс","^",50,25,5 if player.level.get()==1 else 0,[["(x^5)'=","5x^4"],
                                                                             ["тіло рухається за законом s(t)=5t знайдіть закон швидкості","5"],
                                                                             ["x^2-5x+6=0 в відповідь запишіть суму коренів","5"],
                                                                             ["2^4x-5*2^2x+6=0 в відповідь запишіть раціональний корінь в вигляді десяткового дробу через кому","0,5"],
                                                                             ["sin(pi)","0"]],[[".","^","@","#","#","#","#","@","^","."]])
nps.add(nps1)
nps.add(nps2)

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

controler=Controller("")

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

while not controler.value=="e":
    player.move(controler.value)

    camera.x=player.x-5
    camera.y=player.y-5

    startMap.colision(player)

    cold.colision(player,controler)
    nps.colision(player,controler,player.level.get())


    scene.renderMap()

    print("if you want exit you need write e")
    if(not controler.value=="e"):
        controler.value=input("controler:").lower()


