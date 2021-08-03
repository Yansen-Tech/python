class Hero:

    def __init__(self,name,health):
        self.nama= name
        self.health=health

    def showInfo(self):
        print("Show info di class Hero")
        print("{} dengan health {} " .format(
            self.nama,
            self.health
               )
            )

class HeroAbility(Hero):
    def __init__(self,name):
        super().__init__(name,300)
        

    #Override
    def showInfo(self):
        print("Showinfo di subclass Hero ability")
        print("{} \n\ttipe = Ability, \n\tHealth {}".format(
            self.nama,
            self.health
            )
        )

class HeroStrength(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
       
   


Tara=HeroAbility("Tara")
Murad=HeroStrength("Murad")



Tara.showInfo()
Murad.showInfo()