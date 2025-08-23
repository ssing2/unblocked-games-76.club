#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML标签重复检查工具
检查所有HTML文件中的重复meta标签、语法错误等问题
"""

import os
import re
import glob
from collections import Counter
from typing import List, Dict, Tuple

class HTMLDuplicateChecker:
    def __init__(self, directory: str = "."):
        self.directory = directory
        self.issues = []
        
    def find_html_files(self) -> List[str]:
        """查找所有HTML文件"""
        pattern = os.path.join(self.directory, "*.html")
        return glob.glob(pattern)
    
    def check_duplicate_meta_tags(self, content: str, filename: str) -> List[str]:
        """检查重复的meta标签"""
        issues = []
        
        # 检查Open Graph标签
        og_patterns = [
            r'<meta\s+property="og:type"[^>]*>',
            r'<meta\s+property="og:url"[^>]*>',
            r'<meta\s+property="og:title"[^>]*>',
            r'<meta\s+property="og:description"[^>]*>',
            r'<meta\s+property="og:image"[^>]*>'
        ]
        
        for pattern in og_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if len(matches) > 1:
                tag_type = re.search(r'og:(\w+)', pattern).group(1)
                issues.append(f"重复的Open Graph标签 'og:{tag_type}': 找到 {len(matches)} 个")
        
        # 检查Twitter Card标签
        twitter_patterns = [
            r'<meta\s+property="twitter:card"[^>]*>',
            r'<meta\s+property="twitter:url"[^>]*>',
            r'<meta\s+property="twitter:title"[^>]*>',
            r'<meta\s+property="twitter:description"[^>]*>',
            r'<meta\s+property="twitter:image"[^>]*>'
        ]
        
        for pattern in twitter_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if len(matches) > 1:
                tag_type = re.search(r'twitter:(\w+)', pattern).group(1)
                issues.append(f"重复的Twitter Card标签 'twitter:{tag_type}': 找到 {len(matches)} 个")
        
        # 检查canonical标签
        canonical_matches = re.findall(r'<link\s+rel="canonical"[^>]*>', content, re.IGNORECASE)
        if len(canonical_matches) > 1:
            issues.append(f"重复的canonical标签: 找到 {len(canonical_matches)} 个")
        
        # 检查基本meta标签
        meta_patterns = [
            (r'<meta\s+name="description"[^>]*>', "description"),
            (r'<meta\s+name="keywords"[^>]*>', "keywords"),
            (r'<meta\s+name="author"[^>]*>', "author"),
            (r'<meta\s+name="robots"[^>]*>', "robots")
        ]
        
        for pattern, tag_name in meta_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if len(matches) > 1:
                issues.append(f"重复的meta标签 '{tag_name}': 找到 {len(matches)} 个")
        
        return issues
    
    def check_syntax_errors(self, content: str, filename: str) -> List[str]:
        """检查语法错误"""
        issues = []
        
        # 检查多余的尖括号
        extra_brackets = re.findall(r'>>', content)
        if extra_brackets:
            issues.append(f"发现多余的尖括号 '>>': {len(extra_brackets)} 处")
        
        # 检查未闭合的标签 (简单检查)
        open_tags = re.findall(r'<(\w+)[^>]*(?<!/)>', content)
        close_tags = re.findall(r'</(\w+)>', content)
        
        # 排除自闭合标签
        self_closing = ['meta', 'link', 'img', 'br', 'hr', 'input', 'area', 'base', 'col', 'embed', 'source', 'track', 'wbr']
        open_tags = [tag for tag in open_tags if tag.lower() not in self_closing]
        
        open_counter = Counter(open_tags)
        close_counter = Counter(close_tags)
        
        for tag, count in open_counter.items():
            if close_counter.get(tag, 0) != count:
                diff = count - close_counter.get(tag, 0)
                if diff > 0:
                    issues.append(f"可能未闭合的标签 '<{tag}>': 多了 {diff} 个开放标签")
        
        # 检查title标签格式问题
        title_matches = re.findall(r'<title>(.*?)</title>', content, re.IGNORECASE)
        for title in title_matches:
            if 'unblockedunblocked' in title.lower():
                issues.append(f"标题格式错误: '{title}' (包含'unblockedunblocked')")
            if title.count('unblocked') > 2:
                issues.append(f"标题中'unblocked'重复过多: '{title}'")
        
        return issues
    
    def check_content_structure(self, content: str, filename: str) -> List[str]:
        """检查内容结构问题"""
        issues = []
        
        # 检查空的about部分
        about_pattern = r'<section[^>]*id="about"[^>]*>.*?</section>'
        about_match = re.search(about_pattern, content, re.DOTALL | re.IGNORECASE)
        if about_match:
            about_content = about_match.group(0)
            # 移除HTML标签，检查实际文本内容
            text_content = re.sub(r'<[^>]+>', '', about_content).strip()
            if len(text_content) < 100:  # 如果内容少于100字符
                issues.append("about部分内容过少或为空")
        
        # 检查重复的脚本引用
        script_srcs = re.findall(r'<script[^>]*src="([^"]*)"', content, re.IGNORECASE)
        script_counter = Counter(script_srcs)
        for src, count in script_counter.items():
            if count > 1:
                issues.append(f"重复的脚本引用: '{src}' 出现 {count} 次")
        
        # 检查重复的CSS引用
        css_hrefs = re.findall(r'<link[^>]*href="([^"]*\.css)"', content, re.IGNORECASE)
        css_counter = Counter(css_hrefs)
        for href, count in css_counter.items():
            if count > 1:
                issues.append(f"重复的CSS引用: '{href}' 出现 {count} 次")
        
        return issues
    
    def check_file(self, filepath: str) -> Dict[str, List[str]]:
        """检查单个HTML文件"""
        filename = os.path.basename(filepath)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                with open(filepath, 'r', encoding='gbk') as f:
                    content = f.read()
            except:
                return {filename: ["文件编码错误，无法读取"]}
        except Exception as e:
            return {filename: [f"读取文件时出错: {str(e)}"]}
        
        all_issues = []
        
        # 检查各种问题
        all_issues.extend(self.check_duplicate_meta_tags(content, filename))
        all_issues.extend(self.check_syntax_errors(content, filename))
        all_issues.extend(self.check_content_structure(content, filename))
        
        return {filename: all_issues}
    
    def run_check(self) -> Dict[str, List[str]]:
        """运行完整检查"""
        html_files = self.find_html_files()
        print(f"🔍 找到 {len(html_files)} 个HTML文件")
        print("=" * 60)
        
        all_results = {}
        files_with_issues = 0
        total_issues = 0
        
        for filepath in html_files:
            filename = os.path.basename(filepath)
            print(f"检查: {filename}...", end=" ")
            
            result = self.check_file(filepath)
            issues = result[filename]
            
            if issues:
                print(f"❌ 发现 {len(issues)} 个问题")
                files_with_issues += 1
                total_issues += len(issues)
                all_results.update(result)
            else:
                print("✅ 无问题")
        
        print("=" * 60)
        print(f"📊 检查完成:")
        print(f"   - 总文件数: {len(html_files)}")
        print(f"   - 有问题的文件: {files_with_issues}")
        print(f"   - 总问题数: {total_issues}")
        
        return all_results
    
    def generate_report(self, results: Dict[str, List[str]]):
        """生成详细报告"""
        if not results:
            print("\n🎉 恭喜！所有HTML文件都没有发现问题！")
            return
        
        print(f"\n📋 详细问题报告:")
        print("=" * 60)
        
        for filename, issues in results.items():
            print(f"\n📄 {filename}")
            print("-" * 40)
            for i, issue in enumerate(issues, 1):
                print(f"  {i}. {issue}")
        
        # 问题类型统计
        print(f"\n📈 问题类型统计:")
        print("-" * 40)
        
        issue_types = {}
        for issues in results.values():
            for issue in issues:
                issue_type = issue.split(':')[0]
                issue_types[issue_type] = issue_types.get(issue_type, 0) + 1
        
        for issue_type, count in sorted(issue_types.items(), key=lambda x: x[1], reverse=True):
            print(f"  • {issue_type}: {count} 次")

def main():
    print("🔧 HTML标签重复检查工具")
    print("=" * 60)
    
    checker = HTMLDuplicateChecker()
    results = checker.run_check()
    checker.generate_report(results)
    
    # 生成修复建议
    if results:
        print(f"\n💡 修复建议:")
        print("-" * 40)
        print("1. 对于重复的meta标签，删除多余的重复项")
        print("2. 对于语法错误，修正HTML格式")
        print("3. 对于空的about部分，添加丰富的内容")
        print("4. 对于重复的资源引用，合并或删除重复项")
        print("\n使用 replace_string_in_file 工具来修复这些问题。")

if __name__ == "__main__":
    main()
