#объединить два списка в список кортежей
a = ['a','b','c']
b = [1,2,3]

tuple1 = [(k,v) for k,v in zip(a,b)]
print('кортеж', tuple1)

dict1 = dict(zip(a,b))
print('словарь',dict1)


tuple2 = list(zip(a,b))
print('кортеж', tuple2)