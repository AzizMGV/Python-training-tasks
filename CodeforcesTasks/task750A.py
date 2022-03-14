n, k = list(map(int, input().split()))
i = 1
while i <= n:
    k += 5*i
    if k > 4*60:
        k -= 5 * i
        break
    i += 1

print(i - 1)
