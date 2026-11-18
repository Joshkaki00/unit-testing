import unittest
import pytest
import math
from ..carbon_dating import get_age_carbon_14_dating

def test_get_age_carbon_14_dating_normal_case():
    result = get_age_carbon_14_dating(0.35)
    assert math.isclose(result, 8680.34, abs_tol=0.01)

def test_get_age_carbon_14_dating_zero_or_negative():
    assert math.isnan(get_age_carbon_14_dating(0))
    assert math.isnan(get_age_carbon_14_dating(-1))
