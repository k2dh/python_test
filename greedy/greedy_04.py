'''
greedy 04
만들 수 없는 금액
'''

n = int(input())
coins = list(map(int, input().split()))

coins.sort()

result = 1
for x in coins:
    if result < x:
        break
    result += x
    

print(result)