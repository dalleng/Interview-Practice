from typing import List
import math
from collections import Counter


class Solution:
    def numPairsDivisibleBy60Alternative(self, time: List[int]) -> int:
        solutions = 0

        """
        Counter the occurrences of each value in time.

        In [41]: Counter([30,20,150,100,40])
        Out[41]: Counter({30: 1, 20: 1, 150: 1, 100: 1, 40: 1})
        """
        memo = Counter(time)

        """
        Find the largest value in the list.

        In [42]: max([30,20,150,100,40])
        Out[42]: 150
        """
        largest = max(time)

        for t in time:
            """
            The idea here is to find all the multiples of 60, that could be formed
            summing pairs in the list.

            Let's use the list [30, 20, 150, 100, 40] as an example. Let's say
            the current value for t is 30, then the largest sum in the list in
            which one the values is 30 is 180 (150 + 80).

            multiples = (t + largest) // 60 gives up the amount of multiples of
            60, that are less then 180. In this case, 3 (180 / 60).
            """
            multiples = (t + largest) // 60

            """
            initial = math.ceil(t / 60) helps avoiding cases that do not make sense
            given the input data.

            For example, if t is 150 then 150 / 60 = 2.5. But it does not make sense
            to start generating the multiples of 60 using the multiplier 1 because
            60 - 150 = -90 and there are no negative numbers in the input according to
            the problem statement.
            """
            initial = math.ceil(t / 60)

            for m in range(initial, multiples + 1):
                """
                We loop through all the multiples of 60, 60*1, 60*2, and so on looking if
                (60 * m) minus the current value t could be found in the memo dict, which
                would indicate we can find pair/s of numbers that are multiples of 60.
                """
                target = (60 * m) - t
                if target in memo and memo[target]:
                    """
                    memo[t] * (memo[t] - 1) // 2 is used when we analize numbers that add up to 60.
                    For example, if the list is [30, 30, 30] memo would be {30: 3} but we cannot do
                    memo[t] * memo[target] since it'd give 9 which isn't the right amount of pairs.
                    The formula n * (n-1) / 2 gives the numbers of non-repeating pairs.
                    """
                    solutions += memo[t] * (memo[t] - 1) // 2 if target == t else memo[t] * memo[target]

            """
            Avoids duplicate counts. If we have considered the case 30 + 150, there's no need to
            consider the case 150 + 30 for example.
            """
            memo[t] = 0

        return solutions

        def numPairsDivisibleBy60(self, time: List[int]) -> int:
            memo = {}
            solutions = 0

            """
            Build a dictionary of remainders, find the modulo 60 of every
            number in the time list and count the ones that give the same
            result.
            """
            for t in time:
                remainder = t % 60
                if remainder in memo:
                    memo[remainder] += 1
                else:
                    memo[remainder] = 1

            """
            For each remainder in the list built above, looks if there are other/s
            remainders that would add up to 60.
            """
            for num, occurrences in memo.items():
                complement = 60 - num

                """
                If the numbers are multiples of 60 or add up to 60
                Use the formula n * (n - 1) / 2 to find the non repeating
                pairs.
                """
                if num == 0 or num == complement:
                    solutions += occurrences * (occurrences - 1) // 2
                elif complement in memo:
                    solutions += occurrences * memo[complement]
                    """
                    Setting memo[complement] to 0 helps avoid
                    overcouting. If you have alredy considered the
                    pair 30 + 150, no need to also count 150 + 30.
                    """
                    memo[complement] = 0

            return solutions
