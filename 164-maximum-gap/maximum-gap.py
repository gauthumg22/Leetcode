class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n=len(nums)
        if(n<2):
            return 0
        nums.sort()
        ans=0
        maxii=0
        for i in range(n-1):
            maxii=nums[i+1]-nums[i]
            ans=max(ans,maxii)
        return ans


