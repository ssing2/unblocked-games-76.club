import os
import re

# 设置你的工作目录
root_dir = r'd:\Web2088\unblocked-games-76.club'

# 匹配 <meta name="keywords" ...> 标签的正则
pattern = re.compile(r'\s*<meta\s+name=["\']keywords["\'][^>]*>\s*\n?', re.IGNORECASE)

for dirpath, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.html'):
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            new_content = pattern.sub('', content)
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Removed keywords tag from: {file_path}')