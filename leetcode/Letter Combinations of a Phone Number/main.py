from typing import List


# https://leetcode.com/problems/letter-combinations-of-a-phone-number


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d_to_l = {
                '2': list('abc'),
                '3': list('def'),
                '4': list('ghi'),
                '5': list('jkl'),
                '6': list('mno'),
                '7': list('pqrs'),
                '8': list('tuv'),
                '9': list('wxyz'),
        } 
        combinations = []
        
        def inner(current: str, digits: str):
            if digits == '':
                if current:
                    combinations.append(current)
                return

            for l in d_to_l[digits[0]]:
                inner(current + l, digits[1:])

        inner('', digits)
        return combinations


s = Solution()
print(s.letterCombinations('23'))
