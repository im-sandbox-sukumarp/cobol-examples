"""
Unit tests for control flow programs.

Tests conditional logic and loops.
"""
import subprocess
import sys
from pathlib import Path


IF_PATH = Path(__file__).parent.parent / "control" / "01_if.py"
LOOPS_PATH = Path(__file__).parent.parent / "control" / "02_loops.py"


def test_if_greater_than():
    """Test conditional logic with num1 > num2."""
    result = subprocess.run(
        [sys.executable, str(IF_PATH)],
        input="150\n100\nABC\n",
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "greater than" in result.stdout
    assert "positive" in result.stdout
    assert "alphabetic" in result.stdout
    assert "valid range" in result.stdout


def test_if_equal():
    """Test conditional logic with num1 == num2."""
    result = subprocess.run(
        [sys.executable, str(IF_PATH)],
        input="100\n100\n123\n",
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "equal" in result.stdout
    assert "numeric" in result.stdout


def test_if_less_than():
    """Test conditional logic with num1 < num2."""
    result = subprocess.run(
        [sys.executable, str(IF_PATH)],
        input="50\n100\nmixed123\n",
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "less than" in result.stdout
    # 50 is outside range [100-9999]
    assert "outside valid range" in result.stdout


def test_if_negative():
    """Test conditional logic with negative number."""
    result = subprocess.run(
        [sys.executable, str(IF_PATH)],
        input="-10\n50\ndata\n",
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "negative" in result.stdout


def test_loops_output():
    """Test loops program output structure."""
    result = subprocess.run(
        [sys.executable, str(LOOPS_PATH)],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    
    # Check for inline perform
    assert "HELLO WORLD" in result.stdout
    
    # Check for loop execution (B, C, D appear 2 times before separator)
    assert "B-PARAGRAPH" in result.stdout
    assert "C-PARAGRAPH" in result.stdout
    assert "D-PARAGRAPH" in result.stdout
    
    # Check for separator
    assert "=======" in result.stdout
    
    # Check for fall-through paragraphs
    assert "A-PARAGRAPH" in result.stdout
    assert "E-PARAGRAPH" in result.stdout


def test_loops_paragraph_count():
    """Test that paragraphs execute correct number of times."""
    result = subprocess.run(
        [sys.executable, str(LOOPS_PATH)],
        capture_output=True,
        text=True
    )
    
    lines = result.stdout.split('\n')
    
    # Count B-PARAGRAPH occurrences (should appear 3 times: 2 in loop + 1 fall-through)
    b_count = sum(1 for line in lines if "B-PARAGRAPH" in line)
    assert b_count == 3
    
    # A-PARAGRAPH should appear once (only in fall-through)
    a_count = sum(1 for line in lines if "A-PARAGRAPH" in line)
    assert a_count == 1
