n = int(input())
summa = 0
for i in range (n):
    a, b = map(int, input().split())
    if a > b:
        summa += 1
    elif a < b:
        summa -= 1
    else:
        continue
if summa > 0:
    print('Mishka')
elif summa < 0:
    print('Chris')
else:
    print('Friendship is magic!^^')

