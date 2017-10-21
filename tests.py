# -*- coding: utf8 -*-

import sys
import unittest
from StringIO import StringIO

from mock import Mock, patch


def mocked_input(side_effect=None):
    mocked = Mock(side_effect=side_effect)
    return patch('__builtin__.input', new=mocked)


__all__ = (
    'FirstTaskTests',
)


class FirstTaskTests(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_ok(self):
        with mocked_input([1, 2, 3]) as input_mock:
            import task1_1

        self.assertEqual(input_mock.call_count, 3)
        self.assertEqual(sys.stdout.getvalue().strip(), '6')

    def test_error(self):
        with mocked_input([1, 'cat', 3]) as input_mock:
            with self.assertRaises(ValueError):
                import task1_1

        self.assertEqual(input_mock.call_count, 2)
        self.assertEqual(sys.stdout.getvalue().strip(), '')


if __name__ == "__main__":
    unittest.main()
