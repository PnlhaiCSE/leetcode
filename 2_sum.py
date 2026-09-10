class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result

nums = [3,2,3]
target = 6
kq = Solution().twoSum(nums,target)
print(kq)
