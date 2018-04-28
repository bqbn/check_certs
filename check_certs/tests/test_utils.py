
import unittest
from utils import deep_merge

class TestDeepMerge(unittest.TestCase):
    def test_deep_merge(self):

        # when reaches the max level, it should return b
        max_level = 9
        self.assertEqual(deep_merge({'a': 1}, {'b': 2}, level=max_level), {'b': 2})

        # when a is not a dict
        self.assertEqual(deep_merge(None, {'b': 2}), {'b': 2})

        # when b is not a dict
        self.assertEqual(deep_merge({'a': 1}, None), None)

        # same key overwrites
        self.assertEqual(deep_merge({'a': 1}, {'a': 2}), {'a': 2})
        self.assertEqual(
            deep_merge(
                { 'a': { 'b': 1, 'c': 2, } },
                { 'a': { 'c': 3, } }
            ),
            { 'a': { 'b': 1, 'c': 3 } }
        )

        # different keys merge
        self.assertEqual(deep_merge({'a': 1}, {'b': 2}), {'a': 1, 'b': 2})

        self.assertEqual(
            deep_merge(
                { 'a': { 'b': 1, 'c': 2, } },
                { 'a': { 'd': 3, } }
            ),
            { 'a': { 'b': 1, 'c': 2, 'd': 3, } }
        )

class TestGetArgs(unittest.TestCase):
    def test_get_args(self):
        pass
