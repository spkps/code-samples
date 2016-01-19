import unittest

from hilton.search import search


class SearchTestCase(unittest.TestCase):

    def test_search(self):
        graph = [(1, 2), (2, 1), (2, 3), (3, 2), (3, 4), (4, 3),
                 (3, 5), (5, 3), (5, 6), (6, 5), (6, 7), (7, 6)]

        def cmpltr(goal):
            def _helper(roomid):
                return roomid == goal
            return _helper

        self.assertSequenceEqual(search(graph, 1, cmpltr(3)), [1, 2, 3])

