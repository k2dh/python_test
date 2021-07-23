'''
greedy 06
무지의 먹방 라이브
'''
def solution(food_times, k):
    answer = 0
    next = 0
    for _ in range(k):
      if next == len(food_times):
        next = 0
      if food_times[next] == 0:
        next += 1
      food_times[next] -= 1
      next += 1

    if next != len(food_times) and food_times[next] != 0:
      answer = next
    else:
      while True:
        if next == len(food_times):
          next = 0
        if food_times[next] != 0:
          break
        next += 1
      answer = next
    return answer + 1

if __name__ == '__main__':
    print(solution([3,1,2], 2))