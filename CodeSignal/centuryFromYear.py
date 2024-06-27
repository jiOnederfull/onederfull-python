'''
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
solution(year) = 20;
For year = 1700, the output should be
solution(year) = 17.
'''

# 1 - 100: 1
# 101 - 200: 2
# 1901 - 2000: 20
# 1601 - 1700: 17

def solution(year):
    return (year-1)//100+1

print(solution(1))
print(solution(1905))
print(solution(1601))
print(solution(1700))