class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    

    def twoSum(self):
        for x in self.nums:
            for y in self.nums:
                if x + y == self.target:
                    return [self.nums.index(x), self.nums.index(y)]


numerot = [1,2,3,4]
targetti = 7
solution = Solution(numerot, targetti)

result = solution.twoSum()

print(result)
