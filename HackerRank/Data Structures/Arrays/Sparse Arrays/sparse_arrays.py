#!/usr/bin/env python3

from collections import Counter


def main():
    ctr = Counter()
    N = int(input().strip())

    for _ in range(N):
        s = input().strip()
        ctr[s] += 1

    Q = int(input().strip())
    for _ in range(Q):
        q = input().strip()
        print(ctr[q])


if __name__ == "__main__":
    main()
