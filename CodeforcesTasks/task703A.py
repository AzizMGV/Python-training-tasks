n = int(input())
summa_a, summa_b = 0, 0
for i in range (n):
    a, b = map(int, input().split())
    summa_a += a
    summa_b += b
if summa_a == summa_b:
    print('Friendship is magic!^^')
elif summa_a > summa_b:
    print('Mishka')
else:
    print('Chris')


