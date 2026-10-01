from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = defaultdict(list)
        for s in strs:
            sorted_strs[''.join(sorted(s))].append(s)
        
        grps = [sorted_strs[key] for key in sorted_strs.keys()]
        return grps





        