import pytest
from app import CounterApp

def test_counter_increment(qtbot):
    # Initialize the widget
    window = CounterApp()
    qtbot.addWidget(window)

    # Check initial state
    assert window.label.text() == "0"

    # Simulate a mouse click on the button
    qtbot.mouseClick(window.button, "left")

    # Check if the label updated
    assert window.label.text() == "1"
