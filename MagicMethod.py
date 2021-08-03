class Burung:

    def __init__(self,nama,jumlah):
        self.nama=nama
        self.jumlah=jumlah

    def __repr__(self) -> str:
        return " Debug - Burung {} dengan jumlah {}".format(self.nama,self.jumlah)
    
    def __str__(self) -> str:
        return "Burung = {} dengan jumlah {}".format(self.nama,self.jumlah)
    
    def __add__(self,objek):
        return self.jumlah + objek.jumlah

    @property
    def __dict__(self):
        return "Ini mempunyai nama dan objek"


        

    
        



Makan1=Burung("Elang",69)
Makan2=Burung("Naga",89)

print(Makan1)
print(Makan2)
print(Makan2+Makan1)
print(Makan1.__dict__)

