# 11. Container With Most Water

# giải vui vui O(n^2)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0

        for i in range(len(height)):
            for j in range(i+1,len(height)):
                w = j - i
                h = min(height[i], height[j])
                result = max(result, w*h)
        
        return result

# anh GPT dạy O(n) two pointer
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height) - 1

        while left < right:
            w = right - left
            h = min(height[left], height[right])

            result = max(result, w*h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return result


height = [1,8,6,2,5,4,8,3,7]

print(Solution().maxArea(height))