class magical:

    def __init__ (self,name,cakra,defense):
        self.nama    = name
        self.__cakra   = cakra
        self.__defense = defense
       # self.info="Name {} : \n\t cakra : {} ".format(self.nama,self.__cakra)

    def gethealth(self):
        return self.__cakra

    @property
    def info (self):
        return "Name {} : \n\t cakra : {} ".format(self.nama,self.__cakra)
    @property
    def armor(self):
        pass
        
    @armor.getter
    def armor(self):
        return self.__defense

    @armor.setter
    def armor(self,input):
        self.__defense=input
    @armor.deleter
    def armor(self):
        self.__defense=None

        
 
Madara=magical("Madara",999,899)
print(Madara.gethealth())
print(Madara.info)
Madara.nama="Senju"
print(Madara.info)
print(Madara.armor)
Madara.armor=999999
print(Madara.armor)
print(Madara.__dict__)
del Madara.armor
print(Madara.__dict__)