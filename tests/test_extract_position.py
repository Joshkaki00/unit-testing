import pytest
from extract_position import extract_position

def test_extract_position_with_x():
    """Pulls the value after x: from an update line."""
    line = '|update| the positron location in the particle accelerator is x:21.432'
    assert extract_position(line) == '21.432'

def test_extract_position_error_line():
    """Error lines should not yield a position."""
    line = '|error| numerical calculations could not converge.'
    assert extract_position(line) is None

def test_extract_position_debug_line():
    """Debug lines should not yield a position."""
    assert extract_position('|debug| something x:99') is None
