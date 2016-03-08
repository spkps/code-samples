from functools import partial
from operator import getitem


def deepop(op, data, path, *args):

    if not isinstance(data, dict):
        raise ValueError(
            'Invalid data type: {}. Expected is dict'
            .format(type(data).__name__)
            )

    first_dot = path.find('.')
    if first_dot < 0:
        return op(data, path, *args)
    data = data[path[:first_dot]]
    return deepop(op, data, path[first_dot+1:])


deep_get = partial(deepop, getitem)


# Test Zone

from unittest import TestCase, skip


class DeepGetTest(TestCase):

    def test_simple_path(self):

        data = dict(a=1, b=2, cdf=dict(c=3, d=4, f=5))

        a = deep_get(data, 'a')
        self.assertEqual(a, 1)

        d = deep_get(data, 'cdf.d')
        self.assertEqual(d, 4)

    @skip("operator.getitem doen't allow default argument")
    def test_get_default(self):

        data = dict()
        a = deep_get(data, 'a', 1)
        self.assertEqual(a, 1)

    def test_not_dict_data(self):
        data = 'some_kind_of_test_data'
        with self.assertRaises(ValueError):
            result = deep_get(data, 'key.a')
