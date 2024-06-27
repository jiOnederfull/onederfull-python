def solution(a):
    dup = {}
    min_index = len(a)
    answer = -1

    for i, num in enumerate(a):
        if num in dup:
            if i < min_index:
                min_index = i
                answer = num
        else:
            dup[num] = i
    
    return answer

print(solution([2, 1, 3, 5, 3, 2]))  # 출력: 3
print(solution([2, 2]))              # 출력: 2
print(solution([2, 4, 3, 5, 1]))     # 출력: -1
print(solution([1, 2, 3, 4, 5, 1]))  # 출력: 1
print(solution([1, 1, 2, 2, 3, 3]))  # 출력: 1
print(solution([3, 3, 2, 2, 1, 1]))  # 출력: 3
print(solution([1, 2, 3, 4, 5]))     # 출력: -1
print(solution([5, 4, 3, 2, 1, 5, 1])) # 출력: 5
