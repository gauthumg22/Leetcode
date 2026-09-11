class Solution:
    def isBalanced(self, num: str) -> bool:
        esum=osum=0
        n=len(num)
        for i in range(n):
            if i%2==0:
                esum+=int(num[i])
            else:
                osum+=int(num[i])
        return esum==osum
        