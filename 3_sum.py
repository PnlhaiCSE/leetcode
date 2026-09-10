# 15. 3Sum

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)-2):
            if nums[i] == nums[i-1] and i > 0:
                continue
            target = 0 - nums[i]
            left = i + 1 
            right = len(nums) - 1
            while left < right:
                current = sum([nums[left], nums[right]])
                if current == target:
                    out.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif current < target:
                    left += 1
                elif current > target:
                    right -= 1

        return out


nums = [-1,0,1,2,-1,-4]
nums = [0,0,0,0,0]

print(Solution().threeSum(nums))
'''
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''