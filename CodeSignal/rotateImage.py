class rotation:
    def clockwise(self, a):
        answer = list(zip(*a[::-1])) # clockwise
        return answer
    
    def counterclockwise(self, a):
        answer = list(reversed(list(zip(*a)))) # counterclockwise
        return answer
    

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

r = rotation()
print(r.clockwise(a))
print(r.counterclockwise(a))