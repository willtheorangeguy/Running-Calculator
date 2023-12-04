"""This is a test file for the Running Calculator program."""
# pylint: disable=locally-disabled, wrong-import-position, import-error

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import calculate_distance, display_result


def test_calculate_distance():
    """Test if calculate_distance returns the correct distance and unit."""
    # Test when distance is greater than 1000
    distance, unit = calculate_distance(1500, "meters")
    assert distance == 1.5
    assert unit == "kilometers"

    # Test when distance is less than 1000
    distance, unit = calculate_distance(500, "meters")
    assert distance == 500
    assert unit == "meters"


def test_display_result(capsys):
    """Test if display_result prints the correct output."""
    # Test when unit is "meters"
    display_result(500, "meters", 10, 36)
    captured = capsys.readouterr()
    assert "You traveled 500 meters." in captured.out
    assert (
        "Your speed was 10 meters per second or 36 kilometers per hour." in captured.out
    )

    # Test when unit is "kilometers"
    display_result(1.5, "kilometers", 10, 36)
    captured = capsys.readouterr()
    assert "You traveled 1.5 kilometers." in captured.out
    assert (
        "Your speed was 10 meters per second or 36 kilometers per hour." in captured.out
    )
