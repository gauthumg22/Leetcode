class Solution:
    def maxValue(self, nums: List[int]) -> int:
        n=len(nums)
        v=[nums[i] if i%2==0 else -nums[i] for i in range(n)]
        og=sum(v)

        if n<2:
            return og

        dp1=v[0]
        dp0=float('inf')

        mine=float('inf')

        for i in range(1,n):
            nd1=min(v[i],dp0+v[i])
            nd0=dp1+v[i]

            dp1=nd1
            dp0=nd0

            mine=min(mine,dp0)
        max_delta=max(0,-2*mine)

        return og+max_delta