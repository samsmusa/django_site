class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return print([i,j])
                
                
                
                
                
a = Solution()

a.twoSum([3,2,4], 6)