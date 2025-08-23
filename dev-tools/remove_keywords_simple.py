#!/usr/bin/env python3
"""
批量删除HTML文件中的keywords meta标签
"""

import os
import re
import glob

def remove_keywords_meta_tag(file_path):
    """从HTML文件中删除keywords meta标签"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 匹配keywords meta标签的正则表达式（包括换行符）
        pattern = r'\s*<meta\s+name=["\']keywords["\']\s+content=["\'][^"\']*["\']\s*>\s*\n?'
        
        # 检查是否包含keywords标签
        if re.search(pattern, content, re.IGNORECASE):
            # 删除keywords标签
            new_content = re.sub(pattern, '', content, flags=re.IGNORECASE)
            
            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True
        return False
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return False

def main():
    """主函数"""
    print("Starting batch removal of keywords meta tags...")
    print("=" * 60)
    
    # 获取所有HTML文件
    html_files = glob.glob('*.html')
    
    processed_count = 0
    removed_count = 0
    
    for file_path in html_files:
        # 跳过备份目录
        if 'backup_' in file_path:
            continue
            
        processed_count += 1
        if remove_keywords_meta_tag(file_path):
            removed_count += 1
            print(f"SUCCESS: {file_path} - keywords tag removed")
        else:
            print(f"SKIP: {file_path} - no keywords tag found")
    
    print("=" * 60)
    print(f"Processing complete!")
    print(f"Files processed: {processed_count}")
    print(f"Tags removed: {removed_count}")
    print(f"Success rate: {removed_count/processed_count*100:.1f}%" if processed_count > 0 else "Success rate: 0%")

if __name__ == "__main__":
    main()
