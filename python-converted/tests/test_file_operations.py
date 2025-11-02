"""
Unit tests for file operation programs.

Tests file reading functionality.
"""
import subprocess
import sys
from pathlib import Path


FILE_READ_PATH = Path(__file__).parent.parent / "file" / "01_read.py"
TEST_DATA_FILE = Path(__file__).parent / "test_data" / "persons.txt"


def test_read_file_basic():
    """Test basic file reading."""
    result = subprocess.run(
        [sys.executable, str(FILE_READ_PATH), str(TEST_DATA_FILE)],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "John" in result.stdout
    assert "Jane" in result.stdout
    assert "Bob" in result.stdout
    assert "completed successfully" in result.stdout


def test_read_file_record_format():
    """Test that records are formatted correctly."""
    result = subprocess.run(
        [sys.executable, str(FILE_READ_PATH), str(TEST_DATA_FILE)],
        capture_output=True,
        text=True
    )
    
    lines = result.stdout.split('\n')
    
    # Check first record contains ID
    assert any("001" in line for line in lines)
    assert any("002" in line for line in lines)
    assert any("003" in line for line in lines)


def test_read_file_not_found():
    """Test handling of non-existent file."""
    non_existent = Path(__file__).parent / "test_data" / "nonexistent.txt"
    result = subprocess.run(
        [sys.executable, str(FILE_READ_PATH), str(non_existent)],
        capture_output=True,
        text=True
    )
    assert "not found" in result.stdout.lower() or "error" in result.stdout.lower()


def test_read_file_multiple_records():
    """Test that all records are read."""
    result = subprocess.run(
        [sys.executable, str(FILE_READ_PATH), str(TEST_DATA_FILE)],
        capture_output=True,
        text=True
    )
    
    # Count number of person records (should be 3 in test file)
    lines = [line for line in result.stdout.split('\n') if line.strip() and not line.startswith('Error') and not 'completed' in line.lower() and not 'Warning' in line]
    
    # Should have at least 3 records
    assert len(lines) >= 3
