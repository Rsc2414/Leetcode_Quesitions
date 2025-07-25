class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        ans = float('inf')
        
        for i in nums1:
            for j in nums2:
                if i == j:
                    a = i
                else:
                    a = i * 10
                    a += j
                    b = j * 10
                    b += i
                    a = min(a,b)
                ans = min(ans,a)
        
        return ans
        
