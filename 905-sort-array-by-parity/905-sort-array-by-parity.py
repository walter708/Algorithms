class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         i , j = 0 , len(nums) - 1
        
#         while i < j:
#             if nums[i] % 2 > nums[j] % 2:
#                 nums[i] , nums[j] = nums[j] , nums[i]
            
#             if nums[i] % 2 == 0: i+=1
#             if nums[j] % 2 == 1: j-=1
#         return nums
    # Time complexity O(n)
    # Space complexity O(1)
    
    # OR
    # def sortArrayByParity(self, nums: List[int]) -> List[int]:
    #     return ([i for i in nums if i % 2 == 0 ] + [j for j in nums if j % 2 == 1 ])
    # Time complexity O(n)
    # Space complexity O(1)   
    
    # OR
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key = lambda x : x % 2)
        return nums 

                
        