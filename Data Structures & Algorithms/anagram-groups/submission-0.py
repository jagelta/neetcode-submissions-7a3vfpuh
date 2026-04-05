class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        for i in (strs):
            sr = sorted(i)
            sr = ''.join(map(str, sr))
            maps[sr].append(i)
        print(maps.values())
        return list(maps.values())