class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sumsMap = {}
        
        for key , val in enumerate(nums):
            if (target - val) in sumsMap:
                return [key , sumsMap[target - val]]
            else:
                sumsMap[val] = key
        