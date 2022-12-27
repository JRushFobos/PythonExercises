#allowed queen's moves
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if ((abs(x2 - x1) == abs(y2 - y1)) or 
   ((x1 > x2 or x1 < x2) and y1 == y2) or ((y1 > y2 or y1 < y2) and x1 == x2)):
    print('YES')
else:
    print('NO')
