from GameElement.objectGame import ObjectGame


class Cold(ObjectGame):
    def colision(self,player,controler):
        if (self.x == player.x and self.y == player.y and player.level.get()>=2):
            print("end game")
            controlerPassword = input("пароль від сундука з золотом:").lower()
            if (controlerPassword == "прл"):
                print("Winner")
            else:
                print("Game Over")
            controler.value="e"