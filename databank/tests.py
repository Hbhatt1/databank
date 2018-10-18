from django.test import TestCase
from .cell_counts import *

# Create your tests here.

class SumValidTest(TestCase):
    def test_raw_to_percentage(self):
        assert raw_to_percentage(1, 400) == 0.25
        assert raw_to_percentage(399, 400) == 99.75
        assert raw_to_percentage(200, 400) == 50.0
        assert raw_to_percentage(0, 400) == 0.0
        assert raw_to_percentage(400, 400) == 100.0

        class CountValidTest(TestCase):
            def test_count_validation(self):
                assert are_sum_cell_counts_equal_total(1, 0, 0, 0, 0, 0) == False
                assert are_sum_cell_counts_equal_total(201, 41, 100, 53, 5, 400) == True
                assert are_sum_cell_counts_equal_total(1, 1, 1, 1, 1, 5) == True
                assert are_sum_cell_counts_equal_total(399, 0, 0, 0, 1, 400) == True
                assert are_sum_cell_counts_equal_total(399, 0, 0, 0, 0, 400) == False
