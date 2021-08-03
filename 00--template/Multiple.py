class team:
    def SetTim(self,team):
        self.team = team

    def ShowTeam(self):
        print(self.team)

class type:
    def SetType(self,type):
        self.type=type

    def ShowType(self):
        print(self.type)


class Hero(team,type):
    def __init__(self,name,health):
        self.name=name
        self.health=health


Ryoma=Hero("Ryoma",890)
Ryoma.SetTim("Warrior")
Ryoma.SetType("Assasin")

Ryoma.ShowTeam()
Ryoma.ShowType()
        
