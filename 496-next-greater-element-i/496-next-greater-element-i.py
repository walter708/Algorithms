class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        for i in nums1:
            index = nums2.index(i)
            ind = nums1.index(i)
            for j in range((index+1) , len(nums2)):
                if nums2[j] > i:
                    res[ind] = nums2[j]
                    break
        return res
                
        
        