#Напишите программу, которая считывает целое число, 
#после чего на экран выводится следующее и
#предыдущее целое число с пояснительным текстом.
while True:
    a = input('Imput number')
    if a == 'q':
        print('Goodbay')
        break
    else:
        print('previous number of',a,'=', int(a)-1)
        print('next number of',a, '=', int(a)+1)