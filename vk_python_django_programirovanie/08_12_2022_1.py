a = [0, 1, 0]
b = [1, 1, 0]
s = 0

for x in (a, b, a):
    s += x.count(1)

print(s)