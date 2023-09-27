def createCanvas(width,height):
    map=[(["."]*width) for i in range(height)]
    return map

def pushObjectToCanvas(canvas,x,y,element):
    if(y<len(canvas) and x<len(canvas[0]) and x>=0 and y>=0):
        canvas[y][x]=element

def drawCanvas(canvas):
    for lineMap in canvas:
        print("".join(lineMap))

playerX=0
playerY=0
coldX=7
coldY=5

controler=""

print("w-move top")
print("s-move down")
print("a-move left")
print("d-move right")
print("п-пірат")
print("9-9(18)(15)(18)(22)(18)")
print("9(17)0(13)(22)(10) 9(18)(15)(18)(22)(18)")
print("алфавіт масив")
print("пароль від сундука з золотом-(19)(20)(15)")
while not controler=="e":
    canvas=createCanvas(10,10)

    pushObjectToCanvas(canvas,coldX,coldY,"з")
    pushObjectToCanvas(canvas, playerX, playerY, "п")

    drawCanvas(canvas)


    print("if you want exit you need write e")
    controler=input("controler:").lower()

    if (controler == "w"):
        playerY -= 1
    elif (controler == "s"):
        playerY += 1
    elif (controler == "a"):
        playerX -= 1
    elif (controler == "d"):
        playerX += 1

    if (coldX == playerX and coldY == playerY):
        print("end game")
        controler = input("пароль від сундука з золотом:").lower()
        if(controler=="прл"):
            print("Winner")
        else:
            print("Game Over")
        controler="e"

