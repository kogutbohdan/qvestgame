from TehnoObject.arrayFunctions import removeElementInArray


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
        removeElementInArray(self.__gameObjects,object)

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