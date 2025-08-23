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
        print(f"❌ 处理文件 {file_path} 时出错: {e}")
        return False

def main():
    """主函数"""
    print("🚀 开始批量删除keywords meta标签...")
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
            print(f"✅ {file_path} - keywords标签已删除")
        else:
            print(f"⏭️  {file_path} - 未找到keywords标签")
    
    print("=" * 60)
    print(f"📊 处理完成！")
    print(f"   - 处理文件数: {processed_count}")
    print(f"   - 删除标签数: {removed_count}")
    print(f"   - 清理率: {removed_count/processed_count*100:.1f}%" if processed_count > 0 else "   - 清理率: 0%")

if __name__ == "__main__":
    main()
