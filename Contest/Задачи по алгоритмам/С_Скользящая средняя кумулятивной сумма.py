n = int(input())
list1 = list(map(int, input().split()))
k = int(input())

result = []
current_sum = sum(list1[:k])
print(f'current_sum = {current_sum}')
result.append(current_sum / k)
print(f'result = {result}')

for i in range(k, n):
    print('--------------')
    print(list1[i])
    print(list1[i - k])
    print('--------------')
    current_sum += list1[i] - list1[i - k]
    print(current_sum)
    print('--------------')
    print(f'current_sum_circle = {current_sum}')
    result.append(current_sum / k)
    print(f'result_sum_circle = {result}')

result_str = ' '.join(str(x) for x in result)
print(result_str)
