def num_sum(number):
    try:
        int(number)
        list_numbers=str(number)
        summ=0
        for list_number in list_numbers:
            summ+=int(list_number)
        print(summ)
    except ValueError:
        print ('«Это не целое число».')
   
   
num = input('введи число и я сложу его цифры')
num_sum(num)