def solution(l, k):
    for i in l:
        if i == k:
            del l[l.index(i)]
    return l
    
l = [3, 1, 2, 3, 4, 5]
k = 3
# solution(l, k) = [1, 2, 4, 5]

# l = [1, 2, 3, 4, 5, 6, 7]
# k = 10
# solution(l, k) = [1, 2, 3, 4, 5, 6, 7]
print(l)
print(l.remove(k))
print(l)
print(solution(l, k))
