from collections import Counter


def chars_in_a_not_in_b(ctr_a, ctr_b):
    deletions = 0
    for letter, count in ctr_a.items():
        if letter in ctr_b:
            count_b = ctr_b[letter]
            diff = count - count_b
            if diff > 0:
                deletions += diff
        else:
            deletions += count
    return deletions


def number_needed(a, b):
    deletions = 0
    ctr_a = Counter(a)
    ctr_b = Counter(b)
    deletions += chars_in_a_not_in_b(ctr_a, ctr_b)
    deletions += chars_in_a_not_in_b(ctr_b, ctr_a)
    return deletions


"""
a = input().strip()
b = input().strip()

"""
if __name__ == "__main__":
    assert number_needed("abc", "cde") == 4
    assert number_needed("", "") == 0
    assert number_needed("ab", "ba") == 0
    assert number_needed("aaaa", "bbbb") == 8
