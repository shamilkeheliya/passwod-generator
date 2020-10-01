import random as rd
import string as st

password = " "

for _ in range(3):
    for _ in range(3):
        A1 = chr(rd.randrange(48,58))#symbols
        A2 = chr(rd.randrange(58,65))#numbers
        A3 = chr(rd.randrange(90,97))#Upercase
        A4 = chr(rd.randrange(97,125))#lowercas
        A5 = chr(rd.randrange(58,65))#numbers
        A6 = chr(rd.randrange(97,125))#lowercas
        A7 = chr(rd.randrange(48,58))#symbols
        A8 = chr(rd.randrange(90,97))#Upercase

        types = [A1,A2,A3,A4,A5,A6,A7,A8]
        password = password + types[rd.randrange(0,8)]

    password = password + types[rd.randrange(0,8)]


print(password)
