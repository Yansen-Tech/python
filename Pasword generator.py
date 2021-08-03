import random
 
cinta   =     "abcdefghijklmnopqrstuvwxyz"
tolak   =     "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nomor   =     "0123456789"
simbol  =     "! # @ $ % ^ & * ( ) _ + ? > < ~ ` |  \/"

Aku     =     cinta+tolak+nomor+simbol
lengt   =     16

password= (random.sample(Aku,lengt))

print("password = ",password)