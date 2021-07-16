"""
greedy 03
문자열 뒤집기
"""
string = input()
num0 = 0 #1을 0으로 바꾼 횟수
num1 = 0 #0을 1로 바꾼 횟수

if string[0] == '1':
    num0 += 1
else:
    num1 += 1

for i in range(len(string)-1):
    if string[i] != string[i+1]:
        if string[i+1] == '1':
            num0 += 1
        else:
            num1 += 1

print(num0, num1)
print(min(num0, num1))