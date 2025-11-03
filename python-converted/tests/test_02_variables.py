"""
Unit tests for 02_variables program.

Tests variable declaration and data formatting functionality.
"""
import subprocess
import sys
from pathlib import Path


VARIABLES_PATH = Path(__file__).parent.parent / "basic" / "02_variables.py"


def test_variables_output():
    """Test that program displays formatted table correctly."""
    result = subprocess.run(
        [sys.executable, str(VARIABLES_PATH)],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    
    lines = result.stdout.split('\n')
    
    # Check headers
    assert "lp|    number|   decimal|  currency" in lines[0]
    
    # Check separator line (80 dashes)
    assert lines[1] == "-" * 80
    
    # Check data row format
    assert "01|" in lines[2]
    assert "3721" in lines[2]
    assert "-317.21" in lines[2]
    assert "$" in lines[2] and "317.21" in lines[2]


def test_variables_exit_success():
    """Test that program exits successfully."""
    result = subprocess.run(
        [sys.executable, str(VARIABLES_PATH)],
        capture_output=True
    )
    assert result.returncode == 0


def test_variables_formatting():
    """Test that numeric formatting is correct."""
    result = subprocess.run(
        [sys.executable, str(VARIABLES_PATH)],
        capture_output=True,
        text=True
    )
    
    lines = result.stdout.split('\n')
    data_line = lines[2]
    
    # Verify format: "01|      3721|   -317.21|  $317.21"
    # Line position should be 2 digits
    assert data_line.startswith("01|")
    
    # Number should be right-aligned in 10 character field
    assert "3721" in data_line
    
    # Decimal should show sign and 2 decimal places
    assert "-317.21" in data_line
    
    # Currency should have dollar sign and 2 decimal places
    assert "$" in data_line and "317.21" in data_line
