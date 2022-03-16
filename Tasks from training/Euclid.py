#Solution №1. НОД методом вычитания 

a, b = map(int,input().split())
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print(a)

#Solution №2. НОД при помощи нахождения остатка от деления и НОК

a, b = map(int,input().split())
c = a
d = b
while b>0:
    a,b = b, a%b
print('НОД', a)
print('НОК', int((c*d)/a))
