class Solution:
    def encode(self, strs: List[str]) -> str:
        code = ""
        for string in strs:
            code += f"{len(string)}#{string}"
        return code

    def decode(self, s: str) -> List[str]:
        # Check degenerate case
        if not s:
            return []
        else:
            i = 0
            strs = []
            while i < len(s):
                strlen = ""
                while s[i] != '#':
                    strlen += s[i]
                    i += 1
                # Current char is '#
                i += 1 
                strs.append(s[i:i+int(strlen)])
                i += int(strlen)

        return strs