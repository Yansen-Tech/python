class kyubi:
    __jumlah = 0;

    def __init__(self,name):
        self.__nama=name
        kyubi.__jumlah +=1

    def getmane(self):
        return self.__nama

  #Hanya berlaku untuk objek 
    def nartod(self):
        return kyubi.__jumlah
    #Tidak berlaku untuk objek tapi berlaku untuk class
    def nartod1():
        return kyubi.__jumlah
    #Metodstatic menempel pada objek dan class
    @staticmethod
    def nartod2():
        return kyubi.__jumlah

    @classmethod
    def nartod3(csl):
        return csl.__jumlah







Son=kyubi("Son")
print(Son.getmane())
Junbi= kyubi("Junbi")
print(Junbi.getmane())
Zukaku=kyubi("Zukaku")
print(Zukaku.getmane())
print(Zukaku.nartod())
print(kyubi.nartod1())
print(kyubi.nartod2())
print(kyubi.nartod3())
