import random as rd
import string as st

password = " "

for _ in range(3):
    for _ in range(3):
        A1 = chr(rd.randrange(48,58))#symbols
        A2 = chr(rd.randrange(58,65))#numbers
        A3 = chr(rd.randrange(90,97))#Upercase
        A4 = chr(rd.randrange(97,125))#lowercase
        types = [A1,A2,A3,A4]
        password = password + types[rd.randrange(0,4)]

    password = password + types[rd.randrange(0,4)]

print("password generator")
print(password)
