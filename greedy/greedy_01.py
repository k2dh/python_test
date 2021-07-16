"""
greedy 01
모험가 길드
"""

n = int(input())
adventurer = list(map(int, input().split()))

num = 0
adventurer.sort()
print(adventurer)
group = 0
for i in adventurer:
    group += 1
    if group >= i:
        num += 1
        group = 0

print(num)

