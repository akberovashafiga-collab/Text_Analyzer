import pytest
from text_analyzer import extract_words, read_text_file, analyze_text


def test_extract_words():
    words = extract_words("Прикладна лінгвістика Python.")
    assert len(words) == 3
    assert "python" in words


def test_empty_file_error(tmp_path):
    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        read_text_file(str(empty_file))


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_text_file("no_file.txt")