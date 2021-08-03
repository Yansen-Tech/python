class karyawan :
    "Dasar kelas untuk semua karyawan"
    jumlah_karyawan=0

    def __init__(self,nama,gaji):
        self.nama=nama
        self.gaji=gaji
        karyawan.jumlah_karyawan +=1

    def tampilkan_jumlah(self):
        print("Total karyawan = ",karyawan.jumlah_karyawan)

    def tampilkam_profil(self):
        print("Nama : ",self.nama)
        print("Gaji = ",self.gaji)

    #membuat objek pertama dari kelas karyawan 
karyawan1 = karyawan ("Sarah",1000000)
karyawan2 = karyawan ("Budi",90000000)


karyawan1.tampilkam_profil()
karyawan2.tampilkam_profil()

print("Total karyawan = ",karyawan.jumlah_karyawan)

print("Karyawan._doc_ :",karyawan.__doc__)
print("Karyawan_name_  : ",karyawan.__name__)
print("Karyawan _module_ : ",karyawan.__module__)
print('Karyawan _dict_ :',karyawan.__dict__)
print("Karyawan _bases_  : ",karyawan.__bases__)


print("Penghapusan sampah")
class point :
    def __init__(self,x=0,y=0) -> None:
        self.x=x
        self.y=y

    def _del_(self):
        class_name=self.__class__.__name__
        print(class_name,"dihancurkan")

pt1=point()
pt2=pt1
pt3=pt1
print(id(pt1),id(pt2),id(pt3));
del pt1
del pt2
del pt3


print("Pewarisan (Inheritansi) kelas")

class induk:
    parent_attr=100

    def __init__(self):
        print("Memanggil konstruktor induk")

    def parent_method(self):
        print("Memanggil metode induk")

    def set_attr(self,attr):
        induk.parent_attr=attr

    def get_attr(self):
        print("Attribut induk : ",induk.parent_attr)


class Anak(induk):
    def __init__(self):
        print("Memanggil konstruksi anak")

    def child_method(self):
        print("Memanggil methode anak")

c=Anak() #instansiasi kelas anak
c.child_method() # anak memanggil metodenya
c.set_attr(200) # kembali memanggil metode induk 
c.get_attr() # kembali memanggik metode induk
c.parent_method()# memanggil metode induk


    