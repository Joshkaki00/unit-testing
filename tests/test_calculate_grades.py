from unittest import mock
import math
from calculate_grades import read_input, calculate_stat, print_stat, display_grade_stat

def test_calculate_stat_normal_case():
    """Mean and population SD for [1, 2, 3, 4, 5]."""
    mean, sd = calculate_stat([1, 2, 3, 4, 5])
    assert math.isclose(mean, 3.0)
    assert math.isclose(sd, math.sqrt(2.0))
