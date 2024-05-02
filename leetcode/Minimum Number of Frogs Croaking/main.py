class Solution:
    letter_to_index = {letter: i for i, letter in enumerate("croak")}

    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        counts = [0 for _ in range(len("croa"))]
        index_for_letter = {letter: i for i, letter in enumerate("croak")}
        max_frogs = 0
        frogs = 0

        for letter in croakOfFrogs:
            max_frogs = max(max_frogs, frogs)

            if letter == "c":
                counts[0] += 1
                frogs += 1
            elif letter == "k":
                counts = [c - 1 for c in counts]
                frogs -= 1
            else:
                idx = index_for_letter[letter]
                previous_letter = "croak"[idx - 1]
                counts[idx] += 1
                if counts[index_for_letter[previous_letter]] <= 0:
                    return -1

        return max_frogs if all(c == 0 for c in counts) else -1


if __name__ == "__main__":
    s = Solution()
    # basic case
    assert s.minNumberOfFrogs("croak") == 1
    # invalid input: incomplete croak
    assert s.minNumberOfFrogs("croa") == -1
    # a single frog that croaked twice
    assert s.minNumberOfFrogs("croakcroak") == 1
    # two frogs croaking simultaneously
    assert s.minNumberOfFrogs("ccrrooaakk") == 2
    # valid subset but not fully valid str
    assert s.minNumberOfFrogs("ccrrooakkcro") == -1
