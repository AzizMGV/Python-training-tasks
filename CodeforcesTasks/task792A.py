# Solution 1

n = int(input())

row = 0
summaCubes = 0
levels = 0

while summaCubes <= n:
    levels += 1
    row += levels
    summaCubes += row
print(levels - 1)

# Solution 2

n = int(input())

row = 0
summaCubes = 0
levels = 0

while summaCubes < n:
    levels += 1
    row += levels
    summaCubes += row
if summaCubes == n:
    print(levels)
else:
    print(levels-1)
