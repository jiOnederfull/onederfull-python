class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        
        first = float('inf')
        second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n  # smallest so far
            elif n <= second:
                second = n  # second smallest
            else:
                return True  # found a triplet
        
        return False
        '''
        minList=[]
        minNum = float('inf')
        for i in range(len(nums)):
            if minNum > nums[i]:
                minNum = nums[i]
            minList.append(minNum)


        maxList=[]
        maxNum = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            if maxNum < nums[i]:
                maxNum = nums[i]
            maxList.insert(0, maxNum)


        for i in range(1, len(nums)-1):
            if minList[i-1] < nums[i] < maxList[i+1]:
                return True
            
        return False
        '''

'''   
# nums = [1,2,3,4,5]
nums = [5,4,3,2,1]
# nums = [2,1,5,0,4,6]
# nums = [9,8,7,6,5,4,3,4,5]


minList=[]
minNum = float('inf')
for i in range(len(nums)):
    if minNum > nums[i]:
        minNum = nums[i]
    minList.append(minNum)



maxList=[]
maxNum = float('-inf')
for i in range(len(nums) - 1, -1, -1):
    print(nums[i])
    if maxNum < nums[i]:
        maxNum = nums[i]
    maxList.insert(0, maxNum)


for i in range(1, len(nums)-1):
    if minList[i-1] < nums[i] < maxList[i+1]:
        print("true")

print("false")
'''

# 9 8 7 6 5 4 3 3 3 min
    
# 9 8 7 6 5 4 3 4 5 origin
    
# 9 8 7 6 5 5 5 5 5 max

s = Solution()
print(s.increasingTriplet([5,4,3,2,1]))