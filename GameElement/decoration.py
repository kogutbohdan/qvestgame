from GameElement.objectGame import ObjectGame


class Decoration(ObjectGame):
    def colision(self,player):
        preveCoords=player.preveCoords
        if(player.x==self.x and player.y==self.y):
            player.x=preveCoords["x"]
            player.y=preveCoords["y"]