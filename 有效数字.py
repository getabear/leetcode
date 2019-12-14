import re
class Solution:
    def isNumber(self, s: str) -> bool:
        pat=re.compile(r"^[\+\-]?(\d+\.\d+|\d+\.|\.\d+|\d+)(e[\+\-]?\d+)?$")
        return True if len(re.findall(pat,s.strip())) else False