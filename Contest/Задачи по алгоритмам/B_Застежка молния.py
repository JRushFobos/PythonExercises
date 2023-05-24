# 9
# 9 3 2 0 1 5 1 0 0
# 3
# Вывод программы
# 4.666666666666667 1.6666666666666667 1.0
# Правильный ответ
# 4.6666666667 1.666666667 1 2 2.333333335 2 0.3333333
n = int(input())
list1 = list(map(int, input().split()))
k = int(input())

result = []
for begin_index in range(0, len(list1) - k + 1):
    end_index = begin_index + k
    current_sum = 0
    for v in list1[begin_index:end_index]:
        current_sum += v
    current_avg = current_sum / k
    result.append(current_avg)

result_str = ' '.join(str(x) for x in result)
print(result_str)

# 7
# 1 2 3 4 5 6 7
# 4
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
