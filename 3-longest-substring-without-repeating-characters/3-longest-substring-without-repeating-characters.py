class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hist = {}
        max_len, start = 0, 0
        
        for i, ch in enumerate(s):
            if ch in hist and start <= hist[ch]:
                start = hist[ch] + 1
            else:
                max_len = max(max_len, i - start + 1)
            
            hist[ch] = i
            

        return max_len