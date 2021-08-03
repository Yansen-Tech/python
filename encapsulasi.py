class Hero:

    __jumlah=0;

    def __init__(self,name,health,attpower,armor):
        self.__name=name
        self.__healthStandar=health
        self.__attpowerStandar=attpower
        self.__armorStandar= armor
        self.__level=1
        self.__exp=0

        self.__healthMax=self.__healthStandar * self.__level
        self.__attpower = self.__attpowerStandar * self.__level
        self.__armor    = self.__armorStandar * self.__level

        self.__health=self.__healthMax

        Hero.__jumlah += 1

    @property
    def info (self):
        return "{} level {}: \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__attpower,self.__armor)
    @property
    def gainExp(self):
        pass
    
    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name,"Level Up")
            self.__level += 1
            self.__exp -=100

            self.__healthMax=self.__healthStandar*self.__level
            self.__attpower=self.__attpowerStandar*self.__level
            self.__armor = self.__armorStandar*self.__level
    def attack(self,musuh):
        self.gainExp=50







vini = Hero("Listra",100,20,90)
murad=Hero("Murad",100,40,50)

print(vini.info)
vini.gainExp=280
print(vini.info)
murad.attack(vini)

murad.gainExp=10
print(murad.info)