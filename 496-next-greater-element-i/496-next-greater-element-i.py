class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1Idx = {v:i for i , v in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []
        
        for i in range(len(nums2)):
            cur = nums2[i]
            
            while stack and cur > stack[-1]:
                val = stack[-1]
                idx = nums1Idx[val]
                res[idx] = cur
                stack.pop()
                
            if cur in nums1Idx:
                stack.append(cur)
        return res

                
                
        
        