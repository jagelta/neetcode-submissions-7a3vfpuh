class Solution:
    def isValid(self, s: str) -> bool:
        tracker = []
        for char in s:
            print(tracker)
            if char == '(':
                tracker.append(')')
            elif char == '[':
                tracker.append(']')
            elif char == '{':
                tracker.append('}')
            elif len(tracker) == 0 or char != tracker[-1]:
                return False
            elif char == tracker[-1]:
                tracker.pop()
        print(len(tracker))
        if len(tracker) == 0:
            return True
        else:
            return False