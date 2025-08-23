#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终项目状态检查 - 验证项目已准备好部署
"""

import os
import glob
from collections import defaultdict

def final_project_check():
    print("🔍 最终项目状态检查")
    print("=" * 50)
    
    # 检查重要配置文件
    critical_files = {
        'vercel.json': 'Vercel配置文件',
        '404.html': '智能404页面',
        'redirect-mapping.json': '重定向映射',
        '.gitignore': 'Git忽略配置',
        'index.html': '主页',
        'robots.txt': 'SEO配置'
    }
    
    print("📋 关键配置文件检查:")
    all_critical_exist = True
    for file, desc in critical_files.items():
        exists = os.path.exists(file)
        size = os.path.getsize(file) if exists else 0
        print(f"   {desc}: {'✅' if exists else '❌'} {f'({size:,} bytes)' if exists else ''}")
        if not exists:
            all_critical_exist = False
    
    # 统计网站文件
    print(f"\n📊 网站文件统计:")
    file_types = {
        'HTML页面': '*.html',
        'CSS样式': '*.css', 
        'JavaScript': ['*.js', '!redirect-checker.js'],
        '图标文件': ['*.ico', '*.png', '*.jpg', '*.gif'],
        '配置文件': ['vercel.json', 'redirect-mapping.json', '.gitignore', 'robots.txt']
    }
    
    total_files = 0
    for category, patterns in file_types.items():
        if isinstance(patterns, str):
            patterns = [patterns]
        
        files = []
        for pattern in patterns:
            if pattern.startswith('!'):
                # 排除文件
                continue
            files.extend(glob.glob(pattern))
        
        # 过滤存在的文件
        existing_files = [f for f in files if os.path.exists(f)]
        file_count = len(existing_files)
        total_files += file_count
        
        print(f"   {category}: {file_count} 个")
    
    print(f"   📁 总计: {total_files} 个文件")
    
    # 检查是否有遗漏的开发文件
    print(f"\n🔍 检查潜在的开发文件:")
    dev_patterns = ['*.py', '*.backup', '*.tmp', '*.log', '*backup*']
    found_dev_files = []
    
    for pattern in dev_patterns:
        found_dev_files.extend(glob.glob(pattern))
    
    if found_dev_files:
        print(f"   ⚠️  发现 {len(found_dev_files)} 个开发文件:")
        for file in found_dev_files[:10]:  # 只显示前10个
            print(f"      - {file}")
    else:
        print("   ✅ 没有发现遗漏的开发文件")
    
    # 检查dev-tools目录
    print(f"\n🛠️ 开发工具目录检查:")
    if os.path.exists('dev-tools'):
        dev_files = len([f for f in os.listdir('dev-tools') if os.path.isfile(os.path.join('dev-tools', f))])
        dev_dirs = len([d for d in os.listdir('dev-tools') if os.path.isdir(os.path.join('dev-tools', d))])
        print(f"   📁 dev-tools/: ✅ ({dev_files} 文件, {dev_dirs} 目录)")
        
        # 检查重要的开发文件
        important_dev_files = [
            'website_analysis.py',
            'verify_vercel_config.py', 
            'DEPLOY_GUIDE.md',
            'website_manifest.md'
        ]
        
        for file in important_dev_files:
            exists = os.path.exists(os.path.join('dev-tools', file))
            print(f"   {file}: {'✅' if exists else '❌'}")
    else:
        print("   ❌ dev-tools 目录不存在")
    
    # 检查.gitignore配置
    print(f"\n📝 .gitignore配置检查:")
    if os.path.exists('.gitignore'):
        with open('.gitignore', 'r', encoding='utf-8') as f:
            gitignore_content = f.read()
        
        important_ignores = [
            'dev-tools/',
            '*.py',
            '*.backup',
            '*.csv',
            'html_redirects/'
        ]
        
        for pattern in important_ignores:
            if pattern in gitignore_content:
                print(f"   {pattern}: ✅")
            else:
                print(f"   {pattern}: ❌")
    
    # 生成部署检查清单
    print(f"\n📋 部署前检查清单:")
    
    checklist = [
        (all_critical_exist, "所有关键配置文件存在"),
        (len(found_dev_files) == 0, "没有遗漏的开发文件"),
        (os.path.exists('dev-tools'), "开发工具已整理"),
        (os.path.exists('.gitignore'), ".gitignore文件配置"),
        (os.path.exists('vercel.json'), "Vercel配置就绪"),
        (total_files > 200, "网站文件充足")
    ]
    
    passed_checks = sum(1 for check, _ in checklist if check)
    total_checks = len(checklist)
    
    for check, desc in checklist:
        print(f"   {'✅' if check else '❌'} {desc}")
    
    # 最终评分
    score_percentage = (passed_checks / total_checks) * 100
    
    if score_percentage >= 90:
        status = "🏆 优秀 - 准备完毕，可以部署"
        color = "绿色"
    elif score_percentage >= 80:
        status = "🥈 良好 - 基本准备就绪"
        color = "黄色"
    else:
        status = "⚠️ 需要完善后再部署"
        color = "红色"
    
    print(f"\n📊 部署准备度: {passed_checks}/{total_checks} ({score_percentage:.0f}%)")
    print(f"🏆 状态: {status}")
    
    # 生成Git命令
    if score_percentage >= 80:
        print(f"\n🚀 推荐的Git命令:")
        print(f"   git add .")
        print(f"   git status  # 检查要提交的文件")
        print(f"   git commit -m 'Add Vercel redirect configuration and optimize website structure'")
        print(f"   git push origin main")
        print(f"\n⏱️ 预计部署时间: 1-2分钟")
        print(f"🌍 部署后测试URL:")
        print(f"   https://yourdomain.vercel.app/jump-run-games")
        print(f"   https://yourdomain.vercel.app/car-games") 
        print(f"   https://yourdomain.vercel.app/puzzle-games")
    else:
        print(f"\n⚠️ 建议修复上述问题后再部署")
    
    return score_percentage >= 80

if __name__ == "__main__":
    ready = final_project_check()
    print(f"\n{'✅ 项目已准备就绪!' if ready else '❌ 请完善项目后再部署'}")
