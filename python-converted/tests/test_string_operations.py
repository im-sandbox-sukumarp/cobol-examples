"""
Unit tests for string manipulation programs.

Tests concatenation and split functionality.
"""
import subprocess
import sys
from pathlib import Path


CONCAT_PATH = Path(__file__).parent.parent / "string" / "02_concatenation.py"
SPLIT_PATH = Path(__file__).parent.parent / "string" / "03_split.py"


def test_concatenation_basic():
    """Test basic string concatenation."""
    result = subprocess.run(
        [sys.executable, str(CONCAT_PATH)],
        input="John\nDoe\n",
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Result:" in result.stdout
    assert "Position:" in result.stdout


def test_concatenation_with_space():
    """Test concatenation with space delimiter."""
    result = subprocess.run(
        [sys.executable, str(CONCAT_PATH)],
        input="John Smith\nDoe\n",
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    # Should use "John" (up to first space) from first input
    assert "Result:" in result.stdout


def test_split_basic():
    """Test basic string splitting."""
    result = subprocess.run(
        [sys.executable, str(SPLIT_PATH)],
        input="John Doe\n",
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Name: John" in result.stdout
    assert "Surname: Doe" in result.stdout


def test_split_single_token():
    """Test split with only one token."""
    result = subprocess.run(
        [sys.executable, str(SPLIT_PATH)],
        input="John\n",
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Name: John" in result.stdout
    # Surname will be empty or not present


def test_split_multiple_tokens():
    """Test split with more than two tokens."""
    result = subprocess.run(
        [sys.executable, str(SPLIT_PATH)],
        input="John Michael Doe\n",
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Name: John" in result.stdout
    assert "Surname: Michael" in result.stdout
    # "Doe" goes to var-rest (not displayed)
