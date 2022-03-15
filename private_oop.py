class Hero:

    #membuat semua jadi private
    def __init__(self,name,power,armor):
        self.__name = name
        self.__power = power
        self.__armor = armor
        
    #Membuat getter 
    def getName(self):
        return self.__name

    def gethealth(self):
        return self.__power

    #Membuat setter
    def diserang(self,seranganfajar):
         self.__power -= seranganfajar
         
    def setattck(self,nilaibaru):
        self.__armor= nilaibaru


Lunar=Hero("Lunar",100000000000,9000000000)

print(Lunar.getName())
print(Lunar.gethealth())
Lunar.diserang(10000000001)
print(Lunar.gethealth())
Lunar.setattck(1)
print(Lunar.__dict__)
