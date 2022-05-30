class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            index = nums2.index(i)
            check = False
            for j in range((index+1) , len(nums2)):
                if nums2[j] > i:
                    res.append(nums2[j])
                    check =True
                    break
            if check == False:
                res.append(-1)
        return res
                
        
        