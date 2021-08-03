def tambah(a,b):
   return a+b
def kurang(a,b):
   return a-b
def kali(a,b):
    return a*b
def bagi(a,b):
   return a/b
def modulus(a,b):
  return  a%b

print("Kalkulator sederhana")

nilai=int(input("Masukkan nilai = "))
operator=input("Masukkan operator = ")
nilai2=int(input("Masukkan nilai ke 2 = "))

if operator =='+':
    print(nilai,"+",nilai2,"=",tambah(nilai,nilai2))
elif operator=='-':
    print(nilai,"-",nilai2,"=",kurang(nilai,nilai2))
elif operator=='*':
    print(nilai,"*",nilai2,"=",kali(nilai,nilai2))
elif operator=='/':
    print(nilai,"/",nilai2,"=",bagi(nilai,nilai2))
elif operator=="%":
    print(nilai,"%",nilai2,"=",modulus(nilai,nilai2))
else:
    print("Invalid input")