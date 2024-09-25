from typing import List


def asteroidCollision(asteroids: List[int]) -> List[int]:
    # https://leetcode.com/problems/asteroid-collision/
    state = []
    for current in asteroids:
        while True:
            if not state:
                state.append(current)
            else:
                previous = state[-1]
                if previous > 0 and current < 0:
                    if previous == abs(current):
                        state.pop()
                    elif previous < abs(current):
                        state.pop()
                        continue
                else:
                    state.append(current)
            break
    return state


if __name__ == "__main__":
    assert asteroidCollision([5, 10, -5]) == [5, 10]
    assert asteroidCollision([8, -8]) == []
    assert asteroidCollision([10, 2, -5]) == [10]
