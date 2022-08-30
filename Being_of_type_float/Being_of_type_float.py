def to_float(num):
    try:
        print(float (num))
    except ValueError:
        print('no convert')

num=input('enter values to check')
to_float(num)
