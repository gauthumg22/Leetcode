class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxii=nums[0]
        minii=nums[0]
        ans=nums[0]

        for i in range(1,len(nums)):
            x=nums[i]
            if x<0:
                maxii,minii=minii,maxii
            maxii=max(x,maxii*x)
            minii=min(x,minii*x)
            ans=max(ans,maxii)
        return ans
        