"""
greedy 02
곱하기 혹은 더하기
"""
string = input()
sum = int(string[0])
for i in string:
    i = int(i)
    if i == 0:
        continue
    elif i == 1 or sum == 0:
        sum += i
    else:
        sum *= i
print(sum)

