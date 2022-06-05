class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Map = {val:idx for idx, val in enumerate(nums1)}
        
        stack = []
        ans = [-1] * len(nums1)
        for i in range(len(nums2)):
            
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                idx = nums1Map[val]
                ans[idx] = nums2[i]
                
            if nums2[i] in nums1:
                stack.append(nums2[i])
                
        return ans    
        


                
                
        
        