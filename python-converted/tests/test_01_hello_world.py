"""
Unit tests for 01_hello_world program.

Tests the basic hello world functionality.
"""
import subprocess
import sys
from pathlib import Path


HELLO_WORLD_PATH = Path(__file__).parent.parent / "basic" / "01_hello_world.py"


def test_hello_world_output():
    """Test that program prints 'Hello world!' to stdout."""
    result = subprocess.run(
        [sys.executable, str(HELLO_WORLD_PATH)],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert result.stdout == "Hello world!\n"
    assert result.stderr == ""


def test_hello_world_exit_success():
    """Test that program exits successfully."""
    result = subprocess.run(
        [sys.executable, str(HELLO_WORLD_PATH)],
        capture_output=True
    )
    assert result.returncode == 0
