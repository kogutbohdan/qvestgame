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