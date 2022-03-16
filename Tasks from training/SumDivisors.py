number = int(input())
i = 1
summa=0
while i <= number:
    if number%i==0:
        summa += i
    i+=1
print(summa)


#Программа получает на вход натуральное число N. Нужно найти сумму его делителей.
