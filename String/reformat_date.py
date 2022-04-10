import datetime
import re
class Solution:
    def reformatDate(date: str) -> str:
        return datetime.datetime.strptime(re.sub(r"(st|nd|th|rd)", "", date), "%d %b %Y").strftime("%Y-%m-%d")
        
print(Solution.reformatDate("20th Oct 2052"))