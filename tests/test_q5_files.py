import os
import pytest
from src.q5_files import TextFileAnalyzer

# 生成测试文件 sample.txt
SAMPLE_FILE = "sample.txt"
SAMPLE_CONTENT = """AI is fun.
AI and robots work together.
Machine learning is part of AI.
"""

# 如果 sample.txt 不存在，则自动创建
if not os.path.exists(SAMPLE_FILE):
    with open(SAMPLE_FILE, "w", encoding="utf-8") as f:
        f.write(SAMPLE_CONTENT)


def test_read_all():
    t = TextFileAnalyzer(SAMPLE_FILE)
    assert t.read_all().startswith("AI")


def test_count_lines():
    t = TextFileAnalyzer(SAMPLE_FILE)
    assert t.count_lines() == 3


def test_count_words():
    t = TextFileAnalyzer(SAMPLE_FILE)
    assert t.count_words() == 14


def test_count_specific_word():
    t = TextFileAnalyzer(SAMPLE_FILE)
    assert t.count_word("ai") == 3


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        TextFileAnalyzer("no_such_file.txt").read_all()
