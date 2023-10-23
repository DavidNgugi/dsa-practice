from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

# https://www.lintcode.com/problem/920/

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
# determine if a person could attend all meetings.

# Example1
# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: false
# Explanation: 
# (0,30), (5,10) and (0,30),(15,20) will conflict

# Example2
# Input: intervals = [(5,8),(9,15)]
# Output: true
# Explanation: 
# Two times will not conflict 

def can_attend_meetings(intervals: List[Interval]) -> bool:
    """
    Time -> O(NlogN)
    Space -> O(N)
    """
    n = len(intervals)
    if n == 1:
        return True
    
    canAttend = True

    # sort on start O(nlogn)
    intervals.sort(key=lambda i : i[0])

    # O(N)
    for i in range(n-1):
        if intervals[i][1] > intervals[i+1][0]:
            canAttend = False
            break
            
    print("canAttend", canAttend)
    return canAttend

if __name__ == "__main__":
    intervals = [(0,30),(5,10),(15,20)]
    output = False

    print(can_attend_meetings(intervals) == output)

    intervals2 = [(5,8),(9,15)]
    output2 = True

    print(can_attend_meetings(intervals2) == output2)