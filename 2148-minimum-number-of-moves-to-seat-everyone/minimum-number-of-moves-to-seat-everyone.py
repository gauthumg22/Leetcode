class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        pos=0
        for i in range(len(students)):
            if(students[i]!=seats[i]):
                pos+=abs(students[i]-seats[i])
        return pos
