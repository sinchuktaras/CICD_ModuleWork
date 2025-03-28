import pytest
import os
from filtering.filtering_file import filter_file

# Фікстура для створення тимчасових файлів
@pytest.fixture
def temporary_files():
    input_file = "test_input.txt"
    output_file = "filtered.txt"
    
    # Створення тестового файлу з вмістом
    with open(input_file, 'w') as f:
        f.write("Hello world\n")
        f.write("Python is awesome\n")
        f.write("Keyword present here\n")
        f.write("Another line\n")
    
    yield input_file, output_file
    
    # Видалення файлів після тесту
    os.remove(input_file)
    os.remove(output_file)

# Параметризований тест для фільтрації файлу
@pytest.mark.parametrize("keyword, expected_lines", [
    ("Keyword", ["Keyword present here\n"]),
    ("Python", ["Python is awesome\n"]),
    ("Hello", ["Hello world\n"]),
    ("Nonexistent", [])
])
def test_filter_file(temporary_files, keyword, expected_lines):
    input_file, output_file = temporary_files
    filter_file(input_file, keyword, output_file)
    
    # Перевірка результату
    with open(output_file, 'r') as f:
        result_lines = f.readlines()
    
    assert result_lines == expected_lines
