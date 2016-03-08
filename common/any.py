
class AnyMetaType(type):

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return False


class AnyType(object):

    __metaclass__ = AnyMetaType

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return False

ANY = AnyType()

# Test Zone

from unittest import TestCase, skip


class AnyTest(TestCase):

    def test_any(self):

        self.assertEqual(1, ANY)
        self.assertEqual(ANY, 1)

        self.assertEqual('dsaasdsa', ANY)
        self.assertEqual(ANY, '3232423234')

        self.assertEqual(type(int), type(ANY))
        self.assertEqual(type(str), type(ANY))

        self.assertFalse(1 != ANY)
        self.assertFalse(ANY != 1)

        self.assertFalse('dsaasdsa' != ANY)
        self.assertFalse(ANY != '3232423234')

        self.assertFalse(type(int) != type(ANY))
        self.assertFalse(type(str) != type(ANY))
