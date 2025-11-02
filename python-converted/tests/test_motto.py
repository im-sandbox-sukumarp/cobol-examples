"""
Unit tests for motto program.

Tests the GnuCOBOL motto display.
"""
import subprocess
import sys
from pathlib import Path


MOTTO_PATH = Path(__file__).parent.parent / "basic" / "motto.py"


def test_motto_output():
    """Test that motto program displays 'GnuCOBOL'."""
    result = subprocess.run(
        [sys.executable, str(MOTTO_PATH)],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "GnuCOBOL" in result.stdout


def test_motto_exit_success():
    """Test that motto program exits successfully."""
    result = subprocess.run(
        [sys.executable, str(MOTTO_PATH)],
        capture_output=True
    )
    assert result.returncode == 0
