a1 = int(input())
a2 = int(input())
a3 = int(input())
if a1 == a2 == a3:
    print('Равносторонний')
elif a2 == a3 or a1 == a3 or a1 == a2:
    print('Равнобедренный')
else:
    print('Разносторонний')