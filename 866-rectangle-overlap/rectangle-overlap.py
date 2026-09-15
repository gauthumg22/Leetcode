class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1=[rec1[0],rec1[2]] 
        y1=[rec1[1],rec1[3]]
        x2=[rec2[0],rec2[2]]
        y2=[rec2[1],rec2[3]]

        for i in range(2):
            if x1[1]<=x2[0] or x2[1]<=x1[0] or y1[1]<=y2[0] or          y2[1]<=y1[0]:
                return False
        return True 