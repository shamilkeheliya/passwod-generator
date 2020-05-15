import random as rd
import string as st

password = " "

for _ in range(3):
    for _ in range(3):
        A1 = chr(rd.randrange(32,48))#symbols
        A2 = chr(rd.randrange(48,58))#numbers
        A3 = chr(rd.randrange(65,90))#Upercase
        A4 = chr(rd.randrange(97,123))#lowercase
        types = [A1,A2,A3,A4]
        password = password + types[rd.randrange(0,3)]

    password = password + types[rd.randrange(0,3)]


print(password)