"""
Unit tests for 03_add program.

Tests basic addition functionality with user input.
"""
import subprocess
import sys
from pathlib import Path


ADD_PATH = Path(__file__).parent.parent / "basic" / "03_add.py"


def test_add_basic():
    """Test basic addition: 5 + 10 = 15."""
    result = subprocess.run(
        [sys.executable, str(ADD_PATH)],
        input="5\n10\n",
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Enter number 1:" in result.stdout
    assert "Enter number 2:" in result.stdout
    assert "Result : 15" in result.stdout


def test_add_zero():
    """Test addition with zeros: 0 + 0 = 0."""
    result = subprocess.run(
        [sys.executable, str(ADD_PATH)],
        input="0\n0\n",
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Result : 0" in result.stdout


def test_add_large_numbers():
    """Test addition with large numbers: 999999999 + 1 = 1000000000."""
    result = subprocess.run(
        [sys.executable, str(ADD_PATH)],
        input="999999999\n1\n",
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Result : 1000000000" in result.stdout


def test_add_single_operand_zero():
    """Test addition with one zero: 0 + 100 = 100."""
    result = subprocess.run(
        [sys.executable, str(ADD_PATH)],
        input="0\n100\n",
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Result : 100" in result.stdout


def test_add_invalid_input():
    """Test that invalid input produces error message."""
    result = subprocess.run(
        [sys.executable, str(ADD_PATH)],
        input="abc\n10\n",
        capture_output=True,
        text=True
    )
    # Program should handle error gracefully
    assert "Error" in result.stdout or result.returncode != 0
