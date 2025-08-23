#!/usr/bin/env python3
"""
清理HTML文件中的多余空行
保留必要的结构性空行，删除连续的多余空行
"""

def clean_empty_lines(file_path):
    """清理文件中的多余空行"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    cleaned_lines = []
    prev_line_empty = False
    
    for line in lines:
        # 检查是否为空行（只包含空白字符）
        is_empty = line.strip() == ''
        
        # 如果当前行不是空行，或者是第一个空行，则保留
        if not is_empty or not prev_line_empty:
            cleaned_lines.append(line)
        
        prev_line_empty = is_empty
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)
    
    return len(lines) - len(cleaned_lines)

if __name__ == "__main__":
    file_path = "tower-defense-games.html"
    removed_lines = clean_empty_lines(file_path)
    print(f"已清理 {removed_lines} 行多余空行")
