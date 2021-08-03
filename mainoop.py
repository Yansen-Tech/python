class hero:
    
    def __init__(self,name,punch,kick,exployed):
     self.nama=name
     self.pukul=punch
     self.tendang=kick
     self.meledak=exployed
 
    def serang(self,lawan):
        print(self.nama+" menyerang "+lawan.nama)
        lawan.diserang(self,self.nama)

    def diserang(self,lawan,tendanganmaut):
        print(self.nama+" diserang "+lawan.nama)
        tendanganditerima=tendanganmaut/self.pukul
        print("Tendangan diterima serasa = "+str(tendanganditerima))
        self.meledak-=tendanganditerima
        print("Darah "+self.nama+" tersisa "+str(self.meledak))

Zephys=hero("Zephys",100,90,190)
Murad=hero("Murad",90,80,100)

Zephys.serang(Murad)

