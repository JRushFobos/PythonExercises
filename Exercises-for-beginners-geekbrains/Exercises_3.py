from operator  import itemgetter
dict1= {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

result = dict(sorted(dict1.items(), key=itemgetter(1)))
print(result)
result = dict(sorted(dict1.items(), key=itemgetter(1),reverse=True))
print(result)
        