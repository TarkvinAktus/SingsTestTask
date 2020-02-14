
import itertools

numbers = '9876543210'
signs = {'0':'', '1':'+', '2':'-'}
result_sum = 200

signs_list = list(itertools.product('012', repeat=len(numbers)))

for i in signs_list:
    result = ''
    for j in range(len(numbers)-1):
        result += signs[i[j]]
        result += numbers[j]
    result += numbers[j+1]

    #dont count cases with first + sign
    if result[0] != signs['1']:
        sum = eval(result)

        if sum == result_sum:
            print(result + " = 200")