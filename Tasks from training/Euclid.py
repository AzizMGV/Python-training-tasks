#Solution №1. НОД методом вычитания 

a, b = map(int,input().split())
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print(a)

#Solution №2. НОД при помощи нахождения остатка от деления

a, b = map(int,input().split())
while b>0:
    c = a % b
    a,b = b, c
print(a)
