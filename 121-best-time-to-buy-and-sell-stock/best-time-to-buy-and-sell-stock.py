class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=prices[0]
        pr=0
        for p in prices:
            mp=min(mp,p)
            pr=max(pr,p-mp)
        return pr
        