import datetime

class Solution:
    def daysBetweenDates(date1: str, date2: str) -> int:

        d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
        diff = abs(d1 - d2)
        
        return diff.days

print (Solution.daysBetweenDates( "2019-06-29", "2019-06-30"))