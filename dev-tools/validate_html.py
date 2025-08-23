#!/usr/bin/env python3
"""
简单的HTML标签验证脚本，专门检查friday-night-funkin-unblocked.html
"""

import re

def check_html_tags(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找所有HTML标签
    tags = re.findall(r'<(\w+)[^>]*>|</(\w+)>', content)
    
    tag_counts = {}
    for tag in tags:
        if tag[0]:  # 开放标签
            tag_name = tag[0].lower()
            tag_counts[tag_name] = tag_counts.get(tag_name, [0, 0])
            tag_counts[tag_name][0] += 1
        elif tag[1]:  # 闭合标签
            tag_name = tag[1].lower()
            tag_counts[tag_name] = tag_counts.get(tag_name, [0, 0])
            tag_counts[tag_name][1] += 1
    
    print(f"标签平衡检查: {filepath}")
    print("=" * 50)
    
    issues = []
    for tag, counts in tag_counts.items():
        open_count, close_count = counts
        if open_count != close_count:
            diff = open_count - close_count
            if diff > 0:
                print(f"❌ {tag}: {open_count} 开放, {close_count} 闭合 (多了 {diff} 个开放标签)")
                issues.append(f"{tag}: 多了 {diff} 个开放标签")
            else:
                print(f"❌ {tag}: {open_count} 开放, {close_count} 闭合 (多了 {-diff} 个闭合标签)")
                issues.append(f"{tag}: 多了 {-diff} 个闭合标签")
        else:
            print(f"✅ {tag}: {open_count} 开放, {close_count} 闭合")
    
    return issues

if __name__ == "__main__":
    issues = check_html_tags("friday-night-funkin-unblocked.html")
    if issues:
        print(f"\n发现 {len(issues)} 个问题:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("\n✅ 所有标签都正确平衡!")
