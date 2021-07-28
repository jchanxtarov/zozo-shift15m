import unittest
import shift28m.msgs as M
from shift28m.datasets import SumPricesRegression


class TestSumPricesTabular(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_dataset_corrupted(self):
        with self.assertRaises(RuntimeError, msg=M.DATASET_NOT_FOUND):
            SumPricesRegression(root="./dummy_dir")

    def tearDown(self):
        return super().tearDown()
