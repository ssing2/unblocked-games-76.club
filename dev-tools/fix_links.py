#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复 index.html 中的链接格式不一致问题
将所有以 / 开头的相对链接改为不以 / 开头的相对链接
"""

import re
import os

def fix_links():
    index_file = 'index.html'
    
    if not os.path.exists(index_file):
        print(f"错误：文件 {index_file} 不存在")
        return
    
    # 读取文件内容
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 备份原文件
    backup_file = f'{index_file}.link_backup'
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"已创建备份文件：{backup_file}")
    
    # 统计修改前的链接数量
    absolute_links = re.findall(r'href="/([^/][^"]*\.html)"', content)
    print(f"找到 {len(absolute_links)} 个需要修复的绝对路径链接")
    
    # 修复链接：将 href="/xxx.html" 改为 href="xxx.html"
    fixed_content = re.sub(r'href="/([^/][^"]*\.html)"', r'href="\1"', content)
    
    # 写入修复后的内容
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    # 验证修改结果
    with open(index_file, 'r', encoding='utf-8') as f:
        new_content = f.read()
    
    remaining_absolute = re.findall(r'href="/([^/][^"]*\.html)"', new_content)
    total_links = re.findall(r'href="([^"]*\.html)"', new_content)
    
    print(f"\n修复结果：")
    print(f"- 总链接数：{len(total_links)}")
    print(f"- 修复的链接数：{len(absolute_links)}")
    print(f"- 剩余绝对路径链接：{len(remaining_absolute)}")
    print(f"- 修复状态：{'成功' if len(remaining_absolute) == 0 else '部分成功'}")
    
    if len(remaining_absolute) > 0:
        print("\n仍然存在的绝对路径链接：")
        for link in remaining_absolute[:10]:  # 只显示前10个
            print(f"  - /{link}")
    
    # 显示修复的链接示例
    if len(absolute_links) > 0:
        print(f"\n修复的链接示例（前5个）：")
        for i, link in enumerate(absolute_links[:5]):
            print(f"  {i+1}. /{link} -> {link}")

if __name__ == "__main__":
    fix_links()
