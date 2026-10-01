class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        l=[]
        for i in points:
            l.append(i[0])
        l.sort()

        wid=0
        ans=0
        for i in range(len(l)-1):
            wid=l[i+1]-l[i]
            ans=max(ans,wid)
        return ans



        