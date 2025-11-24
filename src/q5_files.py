"""
出题者：柳文章，安徽大学人工智能学院
出题日期：2025.11.22

请设计一个类 ``TextFileAnalyzer``，用于分析纯文本文件（例如 .txt）。

类应包含以下功能：
- 构造方法
- 方法 1：读取整个文件内容
- 方法 2：统计行数
- 方法 3：统计单词数量
- 方法 4：统计某个单词出现次数（不区分大小写）
"""

import os


import string

class TextFileAnalyzer:
    # TODO: 按要求在下方完成程序



if __name__ == "__main__":
    # 以下是运行示例：
    # 生成测试文件 sample.txt
    SAMPLE_FILE = "sample.txt"
    SAMPLE_CONTENT = """Hi, my name is Bob, I am good at coding with Python. 
    Python is a very good programming language"""

    # 如果 sample.txt 不存在，则自动创建
    if not os.path.exists(SAMPLE_FILE):
        with open(SAMPLE_FILE, "w", encoding="utf-8") as f:
            f.write(SAMPLE_CONTENT)

    t = TextFileAnalyzer(SAMPLE_FILE)
    assert t.read_all().startswith("Hi")
