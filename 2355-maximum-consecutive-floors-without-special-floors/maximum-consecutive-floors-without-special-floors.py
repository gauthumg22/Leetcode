class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: list[int]) -> int:
        special.sort()
        ans=0
        ans=max(ans,special[0]-bottom)
        for i in range(1,len(special)):
            ans=max(ans,special[i]-special[i-1]-1)
        ans=max(ans,top-special[-1])
        return ans
