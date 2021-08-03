from typing import Dict


Dictionary={'Nama':'Budi','Kelas':12,'Agama':'Kristen Protestan','Umur':27,'Status':'Mahasiswa',}

print("Nama   : ",Dictionary.get('Nama'))
print("Kelas  : ",Dictionary.get("Kelas"))
print("Agama  : ",Dictionary.get("Agama"))
print("Umur   : ",Dictionary.get("Umur"))
print("Status : ",Dictionary.get("Status"))


Dictionary.clear()

print(Dictionary)


print("=====     F       ===========================      F       ============")
print("==========     U       ==================     U     ==================")
print("===============      N      =====      N      ========================")
print("=====================          G            =======================")
print("=====================      S ======S      ==================")
print("================     I ================  I ============")



def anggur (buah,sayur):
    makanan=buah*sayur
    print(buah,"*",sayur," maka hasilnya adalah ",makanan)
    return makanan

anggur(12,10)


print("N","A","G","A",sep = '&',end='#',)