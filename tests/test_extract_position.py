import pytest
from extract_position import extract_position

def test_extract_position_with_x():
    """Pulls the value after x: from an update line."""
    line = '|update| the positron location in the particle accelerator is x:21.432'
    assert extract_position(line) == '21.432'
