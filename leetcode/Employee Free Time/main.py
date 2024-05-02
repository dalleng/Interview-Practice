import heapq
import unittest


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

    @property
    def as_tuple(self):
        return (self.start, self.end)


class Solution:
    def employeeFreeTime(self, schedule: "[[Interval]]") -> "[Interval]":
        sorted_schedule = []
        for intervals in schedule:
            for interval in intervals:
                heapq.heappush(sorted_schedule, [interval.start, interval.end])

        print(sorted_schedule)

        merged_schedule = []
        while sorted_schedule:
            current = heapq.heappop(sorted_schedule)
            if merged_schedule:
                previous = merged_schedule[-1]

                if current[0] <= previous[1]:
                    previous[1] = max(current[1], previous[1])
                    continue

            merged_schedule.append(current)

        print(merged_schedule)

        free_time = []
        for i in range(len(merged_schedule) - 1):
            current = merged_schedule[i]
            after = merged_schedule[i + 1]
            print(f"current: {current} after: {after}")
            free_time.append(Interval(current[1], after[0]))

        return free_time


class SolutionTestCase(unittest.TestCase):
    def test_example(self):
        schedule = [
            [Interval(*[1, 2]), Interval(*[5, 6])],
            [Interval(*[1, 3])],
            [Interval(*[4, 10])],
        ]
        result = Solution().employeeFreeTime(schedule)
        self.assertEqual(result[0].as_tuple, (3, 4))

    def test_case_1(self):
        schedule = [
            [Interval(*[1, 3]), Interval(*[6, 7])],
            [Interval(*[2, 4])],
            [Interval(*[2, 5]), Interval(*[9, 12])],
        ]
        result = Solution().employeeFreeTime(schedule)
        self.assertEqual([r.as_tuple for r in result], [(5, 6), (7, 9)])


if __name__ == "__main__":
    unittest.main()
