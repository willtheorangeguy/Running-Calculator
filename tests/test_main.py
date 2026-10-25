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


def test_zero_time_reprompts_and_valid_input_still_calculates(monkeypatch, capsys):
    import pytest
    from main import main

    answers = iter(["meters", "1000", "0", "0", "0", "1000", "0", "1", "0", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    with pytest.raises(SystemExit):
        main()
    output = capsys.readouterr().out
    assert "total time greater than zero" in output
    assert "16.67 meters per second" in output
