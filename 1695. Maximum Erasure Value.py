class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        l = 0
        curr = 0
        ans = 0

        for r in range(len(nums)):
            while nums[r] in s:
                s.remove(nums[l])
                curr -= nums[l]
                l += 1
            s.add(nums[r])
            curr += nums[r]
            ans = max(ans,curr)

        return ans
