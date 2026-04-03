class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = list(map(str,t))
        s = list(map(str,s))
        t.sort()
        s.sort()
        if s == t:
            return True
        return False

        