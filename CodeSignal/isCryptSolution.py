def solution(crypt, solution):
    solution_dict = {}
    for i in solution:
        solution_dict[i[0]] = i[1]

    nums = []
    for i in crypt:
        num = str()
        for j in i:
            num += solution_dict[j]
        if len(num) > 1 and num[0] == '0':
            return False
        nums.append(num)

    if int(nums[0])+int(nums[1])==int(nums[2]):
        return True
    else:
        return False


crypt = ["SEND", "MORE", "MONEY"]
a = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]

crypt = ["TEN", "TWO", "ONE"]
a = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]
   

print(solution(crypt, a))
