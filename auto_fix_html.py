#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML标签重复问题自动修复工具
基于check_duplicate_tags.py的检查结果，自动修复常见问题
"""

import os
import re
import glob
import shutil
from datetime import datetime
from typing import List, Tuple

class HTMLAutoFixer:
    def __init__(self, directory: str = "."):
        self.directory = directory
        self.fixed_files = []
        self.backup_dir = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
    def create_backup(self, filepath: str):
        """创建文件备份"""
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
        
        filename = os.path.basename(filepath)
        backup_path = os.path.join(self.backup_dir, filename)
        shutil.copy2(filepath, backup_path)
        print(f"   💾 已备份: {filename}")
    
    def fix_title_format(self, content: str) -> Tuple[str, List[str]]:
        """修复标题格式错误"""
        fixes = []
        
        # 修复 "unblockedunblocked" 问题
        title_pattern = r'<title>(.*?)unblockedunblocked games 76 club</title>'
        match = re.search(title_pattern, content, re.IGNORECASE)
        
        if match:
            game_name = match.group(1).strip()
            if game_name.endswith(' '):
                game_name = game_name.rstrip()
            
            new_title = f'<title>{game_name}unblocked games 76 club</title>'
            content = re.sub(title_pattern, new_title, content, flags=re.IGNORECASE)
            fixes.append(f"修复标题格式: 移除重复的'unblocked'")
        
        return content, fixes
    
    def fix_syntax_errors(self, content: str) -> Tuple[str, List[str]]:
        """修复语法错误"""
        fixes = []
        
        # 修复多余的尖括号
        if '>>' in content:
            content = content.replace('>>', '>')
            fixes.append("修复多余的尖括号 '>>'")
        
        return content, fixes
    
    def remove_duplicate_meta_tags(self, content: str) -> Tuple[str, List[str]]:
        """移除重复的meta标签"""
        fixes = []
        
        # 定义要检查的meta标签模式
        meta_patterns = [
            (r'<meta\s+property="og:type"[^>]*>', "Open Graph type"),
            (r'<meta\s+property="og:url"[^>]*>', "Open Graph URL"),
            (r'<meta\s+property="og:title"[^>]*>', "Open Graph title"),
            (r'<meta\s+property="og:description"[^>]*>', "Open Graph description"),
            (r'<meta\s+property="og:image"[^>]*>', "Open Graph image"),
            (r'<meta\s+property="twitter:card"[^>]*>', "Twitter Card"),
            (r'<meta\s+property="twitter:url"[^>]*>', "Twitter URL"),
            (r'<meta\s+property="twitter:title"[^>]*>', "Twitter title"),
            (r'<meta\s+property="twitter:description"[^>]*>', "Twitter description"),
            (r'<meta\s+property="twitter:image"[^>]*>', "Twitter image"),
            (r'<link\s+rel="canonical"[^>]*>', "Canonical URL"),
            (r'<meta\s+name="author"[^>]*>', "Author meta"),
            (r'<meta\s+name="robots"[^>]*>', "Robots meta"),
        ]
        
        for pattern, name in meta_patterns:
            matches = list(re.finditer(pattern, content, re.IGNORECASE))
            if len(matches) > 1:
                # 保留第一个，删除其余的
                for match in reversed(matches[1:]):  # 从后往前删除避免索引问题
                    start, end = match.span()
                    content = content[:start] + content[end:]
                fixes.append(f"移除重复的{name}标签 ({len(matches)-1}个)")
        
        return content, fixes
    
    def remove_duplicate_css_js(self, content: str) -> Tuple[str, List[str]]:
        """移除重复的CSS和JS引用"""
        fixes = []
        
        # 检查CSS重复
        css_pattern = r'<link[^>]*href="([^"]*\.css)"[^>]*>'
        css_matches = re.findall(css_pattern, content, re.IGNORECASE)
        css_seen = set()
        css_duplicates = []
        
        for css in css_matches:
            if css in css_seen:
                css_duplicates.append(css)
            else:
                css_seen.add(css)
        
        if css_duplicates:
            for css_file in set(css_duplicates):
                # 找到所有匹配项
                full_pattern = f'<link[^>]*href="{re.escape(css_file)}"[^>]*>'
                matches = list(re.finditer(full_pattern, content, re.IGNORECASE))
                
                if len(matches) > 1:
                    # 保留第一个，删除其余的
                    for match in reversed(matches[1:]):
                        start, end = match.span()
                        content = content[:start] + content[end:]
                    fixes.append(f"移除重复的CSS引用: {css_file}")
        
        # 检查JS重复
        js_pattern = r'<script[^>]*src="([^"]*)"[^>]*></script>'
        js_matches = re.findall(js_pattern, content, re.IGNORECASE)
        js_seen = set()
        js_duplicates = []
        
        for js in js_matches:
            if js in js_seen:
                js_duplicates.append(js)
            else:
                js_seen.add(js)
        
        if js_duplicates:
            for js_file in set(js_duplicates):
                full_pattern = f'<script[^>]*src="{re.escape(js_file)}"[^>]*></script>'
                matches = list(re.finditer(full_pattern, content, re.IGNORECASE))
                
                if len(matches) > 1:
                    for match in reversed(matches[1:]):
                        start, end = match.span()
                        content = content[:start] + content[end:]
                    fixes.append(f"移除重复的JS引用: {js_file}")
        
        return content, fixes
    
    def fix_file(self, filepath: str) -> bool:
        """修复单个文件"""
        filename = os.path.basename(filepath)
        
        try:
            # 读取文件
            with open(filepath, 'r', encoding='utf-8') as f:
                original_content = f.read()
        except UnicodeDecodeError:
            try:
                with open(filepath, 'r', encoding='gbk') as f:
                    original_content = f.read()
            except:
                print(f"   ❌ 无法读取文件: {filename}")
                return False
        
        content = original_content
        all_fixes = []
        
        # 应用各种修复
        content, fixes = self.fix_title_format(content)
        all_fixes.extend(fixes)
        
        content, fixes = self.fix_syntax_errors(content)
        all_fixes.extend(fixes)
        
        content, fixes = self.remove_duplicate_meta_tags(content)
        all_fixes.extend(fixes)
        
        content, fixes = self.remove_duplicate_css_js(content)
        all_fixes.extend(fixes)
        
        # 如果有修复，保存文件
        if all_fixes:
            self.create_backup(filepath)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"   ✅ 已修复 {len(all_fixes)} 个问题:")
            for fix in all_fixes:
                print(f"      • {fix}")
            
            self.fixed_files.append((filename, all_fixes))
            return True
        
        return False
    
    def fix_critical_files(self, problem_files: list):
        """修复有问题的文件"""
        print(f"🔧 开始自动修复 {len(problem_files)} 个有问题的文件")
        print("=" * 60)
        
        fixed_count = 0
        
        for filename in problem_files:
            filepath = os.path.join(self.directory, filename)
            if not os.path.exists(filepath):
                continue
                
            print(f"🔨 修复: {filename}")
            
            if self.fix_file(filepath):
                fixed_count += 1
            else:
                print(f"   ⏭️  无需修复或无法修复")
        
        print("=" * 60)
        print(f"📊 修复完成:")
        print(f"   - 尝试修复的文件: {len(problem_files)}")
        print(f"   - 成功修复的文件: {fixed_count}")
        print(f"   - 备份目录: {self.backup_dir}")
        
        return fixed_count
    
    def generate_fix_report(self):
        """生成修复报告"""
        if not self.fixed_files:
            print("\n🎉 没有文件需要修复！")
            return
        
        print(f"\n📋 修复报告:")
        print("=" * 60)
        
        for filename, fixes in self.fixed_files:
            print(f"\n📄 {filename}")
            print("-" * 40)
            for i, fix in enumerate(fixes, 1):
                print(f"  {i}. {fix}")

def main():
    print("🛠️  HTML自动修复工具")
    print("=" * 60)
    
    # 这些是从检查脚本中发现有问题的文件
    problem_files = [
        "crossy-road-unblocked.html",
        "football-masters-unblocked.html", 
        "football-strike-unblocked.html",
        "freecell-solitaire-unblocked.html",
        "fruit-ninja-unblocked.html",
        "fruita-crush-unblocked.html",
        "g-switch-2-unblocked.html",
        "g-switch-3-unblocked.html", 
        "g-switch-4-unblocked.html",
        "g-switch-unblocked.html",
        "geometry-jump-unblocked.html",
        "gobdun-unblocked.html",
        "guess-the-kitty-unblocked.html",
        "hanger-unblocked.html", 
        "happy-fishing-unblocked.html",
        "head-soccer-2023-unblocked.html",
        "heads-arena-soccer-all-stars-unblocked.html",
        "highway-rider-extreme-unblocked.html",
        "hop-pop-it-unblocked.html",
        "icy-purple-head-2-unblocked.html",
        "icy-purple-head-3-unblocked.html",
        "idle-mining-empire-unblocked.html",
        "idle-restaurants-unblocked.html",
        "index.html",
        "moto-x3m-unblocked.html"
    ]
    
    fixer = HTMLAutoFixer()
    fixed_count = fixer.fix_critical_files(problem_files)
    fixer.generate_fix_report()
    
    print(f"\n💡 注意事项:")
    print("-" * 40)
    print("1. 所有修改的文件都已自动备份")
    print("2. 请检查修复后的文件确保正确性")
    print("3. 对于空的about部分，仍需要手动添加内容")
    print("4. 未闭合标签的问题可能需要手动检查")

if __name__ == "__main__":
    main()
