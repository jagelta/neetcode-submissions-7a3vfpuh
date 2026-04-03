class Solution:
    def isPalindrome(self, s: str) -> bool:
        accepted = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9"
        ]
        l = s.strip().lower()
        s = []

        for x in l:
            if x.upper() in accepted:
                s.append(x)

        if len(s) == 2 and s[0] != s[1]:
            return False

        for i, x in enumerate(s):
            if x != s[-i - 1]:
                return False
        
        return True
