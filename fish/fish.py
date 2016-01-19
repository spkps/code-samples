#!/usr/bin/env python

from collections import namedtuple
from itertools import imap, izip

fish = namedtuple('fish', ['size', 'dir'])

def goes_up(f):
    # 0 represents a fish flowing upstream
    return f.dir == 0


def goes_down(f):
    # 1 represents a fish flowing downstream
    return f.dir == 1


def in_opposite(p, q):
    return p.dir == 1 and q.dir == 0


def meet(p, q, downstream=None):
    assert in_opposite(p, q)

    # If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
    if p.size > q.size:
        return p
    # If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
    while downstream:
        p = downstream.pop()
        if p.size > q.size:
            return p
    return q


def solution(sizes, directions):
    # The fish are numbered from 0 to N-1. If P and Q are two fish and P < Q
    # then fish P is initially upstream of fish Q
    # Initially, each fish has a unique position and a unique size
    fishes = imap(lambda f: fish(*f), izip(sizes, directions))
    p = next(fishes)
    count = 1
    downstream = []
    for q in fishes:
        if in_opposite(p, q):
            p = meet(p, q, downstream)
            continue
        if goes_down(p):
            downstream.append(p)
        if goes_up(p):
            count += 1
        p = q
    return count + len(downstream)


def test_solution():
    a = [4, 3, 2, 1, 5]
    b = [0, 1, 0, 0, 0]
    assert solution(a, b) == 2

    a = [1, 3, 2, 4, 5]
    b = [1, 1, 1, 1, 1]
    assert solution(a, b) == 5

    a = [1, 3, 2, 4, 5]
    b = [0, 0, 0, 0, 0]
    assert solution(a, b) == 5

    a = [5, 4, 3, 2, 6, 1]
    b = [1, 1, 1, 1, 0, 0]
    assert solution(a, b) == 2


if __name__ == '__main__':
    test_solution()
