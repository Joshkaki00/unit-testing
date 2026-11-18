from unittest import mock
import math
from calculate_grades import read_input, calculate_stat, print_stat, display_grade_stat

def test_calculate_stat_normal_case():
    """Mean and population SD for [1, 2, 3, 4, 5]."""
    mean, sd = calculate_stat([1, 2, 3, 4, 5])
    assert math.isclose(mean, 3.0)
    assert math.isclose(sd, math.sqrt(2.0))

def test_calculate_stat_empty_list():
    """Empty grade list should return NaN for mean and SD."""
    mean, sd = calculate_stat([])
    assert math.isnan(mean)
    assert math.isnan(sd)

def test_read_input(monkeypatch):
    """read_input collects five integers from input()."""
    answers = iter(['90', '80', '70', '60', '50'])
    monkeypatch.setattr('builtins.input', lambda _: next(answers))
    assert read_input() == [90, 80, 70, 60, 50]

def test_print_stat(capsys):
    """print_stat writes the expected summary lines."""
    print_stat(3.0, math.sqrt(2.0))
    out = capsys.readouterr().out
    assert '****** Grade Statistics ******' in out
    assert "The grades's mean is:" in out
    assert '****** END ******' in out
