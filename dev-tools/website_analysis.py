#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
网站整体状态检查脚本
检查HTML结构、链接格式、性能优化等各方面
"""

import re
import os
from collections import defaultdict

def analyze_website():
    print("🔍 网站整体状态分析")
    print("=" * 60)
    
    # 1. 检查index.html基本信息
    index_file = 'index.html'
    if not os.path.exists(index_file):
        print("❌ index.html 文件不存在")
        return
    
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"📄 index.html 文件大小: {len(content):,} 字符")
    print(f"📄 index.html 行数: {len(content.splitlines()):,} 行")
    
    # 2. 检查HTML结构
    print("\n🏗️ HTML结构检查:")
    doctype = re.search(r'<!DOCTYPE[^>]*>', content)
    html_tag = re.search(r'<html[^>]*>', content)
    head_tag = re.search(r'<head>', content)
    body_tag = re.search(r'<body[^>]*>', content)
    
    print(f"   DOCTYPE声明: {'✅' if doctype else '❌'}")
    print(f"   HTML标签: {'✅' if html_tag else '❌'}")
    print(f"   HEAD标签: {'✅' if head_tag else '❌'}")
    print(f"   BODY标签: {'✅' if body_tag else '❌'}")
    
    # 3. 检查SEO优化
    print("\n🔍 SEO优化检查:")
    title = re.search(r'<title[^>]*>(.*?)</title>', content, re.DOTALL)
    meta_desc = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', content)
    meta_keywords = re.search(r'<meta[^>]*name=["\']keywords["\']', content)
    canonical = re.search(r'<link[^>]*rel=["\']canonical["\']', content)
    
    print(f"   标题标签: {'✅' if title else '❌'} {f'({title.group(1)[:50]}...)' if title else ''}")
    print(f"   描述标签: {'✅' if meta_desc else '❌'}")
    print(f"   关键词标签: {'❌ (已清理)' if not meta_keywords else '⚠️ 仍存在'}")
    print(f"   规范链接: {'✅' if canonical else '❌'}")
    
    # 4. 检查性能优化
    print("\n⚡ 性能优化检查:")
    dns_prefetch = re.findall(r'<link[^>]*rel=["\']dns-prefetch["\']', content)
    preload = re.findall(r'<link[^>]*rel=["\']preload["\']', content)
    lazy_loading = re.findall(r'loading=["\']lazy["\']', content)
    defer_scripts = re.findall(r'<script[^>]*defer[^>]*>', content)
    
    print(f"   DNS预取: {'✅' if dns_prefetch else '❌'} ({len(dns_prefetch)} 个)")
    print(f"   资源预加载: {'✅' if preload else '❌'} ({len(preload)} 个)")
    print(f"   图片懒加载: {'✅' if lazy_loading else '❌'} ({len(lazy_loading)} 个)")
    print(f"   脚本延迟加载: {'✅' if defer_scripts else '❌'} ({len(defer_scripts)} 个)")
    
    # 5. 检查链接格式一致性
    print("\n🔗 链接格式检查:")
    all_links = re.findall(r'href=["\']([^"\']*\.html)["\']', content)
    absolute_links = [link for link in all_links if link.startswith('/')]
    relative_links = [link for link in all_links if not link.startswith('/') and not link.startswith('http')]
    external_links = [link for link in all_links if link.startswith('http')]
    
    print(f"   总链接数: {len(all_links)}")
    print(f"   相对路径: {'✅' if relative_links else '❌'} ({len(relative_links)} 个)")
    print(f"   绝对路径: {'✅ (无)' if not absolute_links else f'⚠️ ({len(absolute_links)} 个)'}")
    print(f"   外部链接: {len(external_links)} 个")
    
    # 6. 检查响应式设计
    print("\n📱 响应式设计检查:")
    viewport = re.search(r'<meta[^>]*name=["\']viewport["\']', content)
    bootstrap = re.search(r'bootstrap', content, re.IGNORECASE)
    media_queries = re.findall(r'@media[^{]*{', content)
    
    print(f"   视口标签: {'✅' if viewport else '❌'}")
    print(f"   Bootstrap框架: {'✅' if bootstrap else '❌'}")
    print(f"   媒体查询: {len(media_queries)} 个")
    
    # 7. 检查无障碍访问
    print("\n♿ 无障碍访问检查:")
    aria_labels = re.findall(r'aria-label=["\'][^"\']*["\']', content)
    alt_texts = re.findall(r'alt=["\'][^"\']*["\']', content)
    
    print(f"   ARIA标签: {'✅' if aria_labels else '❌'} ({len(aria_labels)} 个)")
    print(f"   图片ALT文本: {'✅' if alt_texts else '❌'} ({len(alt_texts)} 个)")
    
    # 8. 统计游戏数量
    print("\n🎮 游戏内容统计:")
    game_links = [link for link in all_links if 'unblocked.html' in link and not link.startswith('http')]
    category_links = [link for link in all_links if 'games.html' in link]
    
    print(f"   游戏页面: {len(game_links)} 个")
    print(f"   分类页面: {len(category_links)} 个")
    
    # 9. 检查文件存在性
    print("\n📁 文件存在性检查:")
    missing_files = []
    for link in relative_links:
        if not os.path.exists(link):
            missing_files.append(link)
    
    print(f"   链接正确性: {'✅ 100%' if not missing_files else f'❌ {len(missing_files)} 个缺失文件'}")
    
    # 10. 总体评分
    print("\n📊 整体评分:")
    score = 0
    max_score = 10
    
    # 评分标准
    if doctype and html_tag and head_tag and body_tag: score += 1
    if title and meta_desc: score += 1
    if not meta_keywords: score += 1  # 没有keywords是好事
    if dns_prefetch or preload: score += 1
    if lazy_loading: score += 1
    if not absolute_links: score += 1  # 链接格式统一
    if viewport: score += 1
    if bootstrap: score += 1
    if aria_labels: score += 1
    if not missing_files: score += 1
    
    percentage = (score / max_score) * 100
    
    if percentage >= 90:
        grade = "🏆 优秀"
    elif percentage >= 80:
        grade = "🥈 良好"
    elif percentage >= 70:
        grade = "🥉 中等"
    else:
        grade = "⚠️ 需改进"
    
    print(f"   得分: {score}/{max_score} ({percentage:.0f}%)")
    print(f"   等级: {grade}")
    
    print("\n✅ 网站分析完成!")

if __name__ == "__main__":
    analyze_website()
