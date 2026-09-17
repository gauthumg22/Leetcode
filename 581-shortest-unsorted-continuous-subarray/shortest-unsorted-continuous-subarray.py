class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        s=sorted(nums)
        left=0
        right=len(nums)-1
        while left<len(nums) and nums[left]==s[left]:
            left+=1
        while right >0 and nums[right]==s[right]:
            right-=1
        if left >right:
            return 0
        return right-left+1