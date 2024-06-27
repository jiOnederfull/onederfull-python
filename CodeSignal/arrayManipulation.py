'''
Given an array a, your task is to output an array b of the same length by applying the following transformation: 
– For each i from 0 to a.length - 1 inclusive, b[i] = a[i - 1] + a[i] + a[i + 1]
– If an element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, use 0 in its place
– For instance, b[0] = 0 + a[0] + a[1]

Example

For a = [4, 0, 1, -2, 3]: 
– b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
– b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
– b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
– b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
– b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1

So, the output should be solution(a) = [4, 5, -1, 2, 1].
Taking a look at this question, you can see that it covers a basic array traversal and manipulation. The candidate simply needs to return the sum of each value in a, plus its right and left neighbors. 

At the same time, the question asks candidates to take into account corner cases with their implementation, which is an important fundamental skill. They need to correctly handle the first and last elements of the array. 
'''


def solution(a):
    b = []
    for i in range(len(a)):
        second = a[i]
        if i-1 == -1:
            first = 0
        else:
            first = a[i-1]
        if i+1 >= len(a):
            third = 0
        else:
            third = a[i+1]
        b.append(first + second + third)

    return b

a = [4, 0, 1, -2, 3]
print(solution(a))



'''
# Answer
def solution(a):
   n = len(a)
   b = [0 for _ in range(n)]
   for i in range(n):
       b[i] = a[i]
       if i > 0:
           b[i] += a[i - 1]
       if i < n - 1:
           b[i] += a[i + 1]
   return b 
'''