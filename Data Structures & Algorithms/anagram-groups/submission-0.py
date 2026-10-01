class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(str1, str2):
            return sorted(str1) == sorted(str2)

        strs = sorted(strs)
        anagram_group = []
        _seen = []
        for i in range(len(strs)):
            if strs[i] in _seen: continue
            anagram_subgroup = []
            _seen.append(strs[i])
            for j in range(len(strs)):
                if isAnagram(strs[i], strs[j]):
                    anagram_subgroup.append(strs[j])
                    _seen.append(strs[j])
            anagram_group.append(anagram_subgroup)
        return anagram_group


            

        