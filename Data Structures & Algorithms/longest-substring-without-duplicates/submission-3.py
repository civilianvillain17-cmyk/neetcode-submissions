class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}          # символ -> его последний индекс
        left = 0
        best = 0
        
        for right, ch in enumerate(s):
            if ch in seen and seen[ch] >= left:
                # сдвигаем левую границу за пределы повторяющегося символа
                left = seen[ch] + 1
            seen[ch] = right
            best = max(best, right - left + 1)
        
        return best
