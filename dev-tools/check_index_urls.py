#!/usr/bin/env python3
"""
检查 index.html 中的所有链接是否对应实际存在的文件
"""

import os
import re
from pathlib import Path

def extract_urls_from_index():
    """从 index.html 提取所有 .html 链接"""
    urls = []
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配所有 href="*.html" 的链接
    pattern = r'href="([^"]*\.html)"'
    matches = re.findall(pattern, content)
    
    for match in matches:
        # 移除开头的 / 如果存在
        url = match.lstrip('/')
        if url not in urls:  # 避免重复
            urls.append(url)
    
    return sorted(urls)

def check_file_exists(url):
    """检查文件是否存在"""
    return os.path.exists(url)

def main():
    """主检查函数"""
    print("检查 index.html 中的所有链接...")
    print("=" * 60)
    
    urls = extract_urls_from_index()
    
    missing_files = []
    existing_files = []
    
    for url in urls:
        if check_file_exists(url):
            existing_files.append(url)
            print(f"✅ {url}")
        else:
            missing_files.append(url)
            print(f"❌ {url} - 文件不存在")
    
    print("=" * 60)
    print(f"📊 检查结果:")
    print(f"   总链接数: {len(urls)}")
    print(f"   存在文件: {len(existing_files)}")
    print(f"   缺失文件: {len(missing_files)}")
    print(f"   正确率: {len(existing_files)/len(urls)*100:.1f}%")
    
    if missing_files:
        print("\n❌ 缺失的文件:")
        for file in missing_files:
            print(f"   - {file}")
    else:
        print("\n🎉 所有链接都对应存在的文件!")
    
    # 保存结果到文件
    with open('url_check_result.txt', 'w', encoding='utf-8') as f:
        f.write("Index.html URL 检查结果\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"总链接数: {len(urls)}\n")
        f.write(f"存在文件: {len(existing_files)}\n")
        f.write(f"缺失文件: {len(missing_files)}\n")
        f.write(f"正确率: {len(existing_files)/len(urls)*100:.1f}%\n\n")
        
        if missing_files:
            f.write("缺失的文件:\n")
            for file in missing_files:
                f.write(f"- {file}\n")
        
        f.write("\n所有检查的URL:\n")
        for url in urls:
            status = "✅" if url in existing_files else "❌"
            f.write(f"{status} {url}\n")

if __name__ == "__main__":
    main()
