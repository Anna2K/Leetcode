class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i, ch in enumerate(strs[0]):
            for string in strs:
                if i >= len(string) or string[i] != ch:
                    return strs[0][:i]
        return strs[0]