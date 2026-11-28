import unittest

from app.compact_list import compact_list


class CompactListTests(unittest.TestCase):
    def test_compact_list_trims_and_drops_empty_values(self):
        self.assertEqual(compact_list([" alpha ", None, "", "beta"]), ["alpha", "beta"])


if __name__ == "__main__":
    unittest.main()
