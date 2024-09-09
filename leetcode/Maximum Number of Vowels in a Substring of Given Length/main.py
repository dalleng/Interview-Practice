class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = 0
        vowels = 0
        start = 0
        
        for i in range(len(s)):

            if s[i] in 'aeiou':
                vowels += 1
            
            if i - start == k:
                if s[start] in 'aeiou':
                    vowels -= 1
                start += 1

            max_vowels = max(max_vowels, vowels)
        
        return max_vowels
        


print(Solution().maxVowels('abciiidef', 3))
