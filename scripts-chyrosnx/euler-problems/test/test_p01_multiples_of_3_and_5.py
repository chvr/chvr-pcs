import unittest
from p01_multiples_of_3_and_5 import MultiplesOfThreeAndFive


class TestMultiplesOfThreeAndFive(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mtf = MultiplesOfThreeAndFive()

    def test_parse_num_valid_inputs(self):
        default_num = 10
        valid_inputs = [1, '2', '3 ', '\t4', ' 5\t ', '6\n', '\r\n7']
        expected_result = [1, 2, 3, 4, 5, 6, 7]

        for i in range(0, len(valid_inputs)):
            result = self.mtf.parse_num(valid_inputs[i], default_num)
            self.assertEqual(result, expected_result[i])

    def test_parse_num_invalid_inputs(self):
        default_num = 10
        invalid_inputs = ['2.4', 'text']
        expected = 10

        for i in invalid_inputs:
            with self.subTest(input=i):
                result = self.mtf.parse_num(i, default_num)
                self.assertEqual(result, expected)

    def test_summations(self):

        self.mtf.solve(10)
        result = self.mtf.sum
        expected = 23

        self.assertEqual(result, expected)

        self.mtf.solve(205)
        result = self.mtf.sum
        expected = 9773

        self.assertEqual(result, expected)

        self.mtf.solve(1020)
        result = self.mtf.sum
        expected = 242250

        self.assertEqual(result, expected)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
