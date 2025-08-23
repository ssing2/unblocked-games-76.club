#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
项目清理脚本 - 整理开发文件，准备生产部署
将开发工具移动到单独目录，只保留网站必需文件
"""

import os
import shutil
import glob
from datetime import datetime

def clean_project():
    print("🧹 开始清理项目目录...")
    print("=" * 50)
    
    # 创建开发工具目录
    dev_dir = "dev-tools"
    if not os.path.exists(dev_dir):
        os.makedirs(dev_dir)
        print(f"📁 创建开发工具目录: {dev_dir}")
    
    # 需要移动的文件类型和文件
    files_to_move = {
        "Python脚本": "*.py",
        "临时文件": "*.tmp",
        "日志文件": "*.log",
        "备份文件": ["*backup*", "*.backup", "*.bak"],
        "结果文件": ["url_check_result.txt", "missing_files_report.txt"],
        "服务器配置": ["redirect_rules.htaccess", "redirect_rules.nginx"],
        "文档文件": ["REDIRECT_SOLUTION.md", "VERCEL_DEPLOYMENT.md"]
    }
    
    moved_count = 0
    
    # 移动文件
    for category, patterns in files_to_move.items():
        if isinstance(patterns, str):
            patterns = [patterns]
        
        category_files = []
        for pattern in patterns:
            category_files.extend(glob.glob(pattern))
        
        if category_files:
            print(f"\n📂 {category}:")
            for file in category_files:
                if os.path.isfile(file):
                    try:
                        destination = os.path.join(dev_dir, os.path.basename(file))
                        # 如果目标文件存在，添加时间戳
                        if os.path.exists(destination):
                            name, ext = os.path.splitext(destination)
                            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                            destination = f"{name}_{timestamp}{ext}"
                        
                        shutil.move(file, destination)
                        print(f"   ✅ {file} → {destination}")
                        moved_count += 1
                    except Exception as e:
                        print(f"   ❌ 移动失败 {file}: {e}")
    
    # 检查并移动备份目录
    backup_dirs = [d for d in os.listdir('.') if 'backup' in d.lower() and os.path.isdir(d)]
    if backup_dirs:
        print(f"\n📁 备份目录:")
        for backup_dir in backup_dirs:
            try:
                destination = os.path.join(dev_dir, backup_dir)
                if os.path.exists(destination):
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    destination = f"{destination}_{timestamp}"
                
                shutil.move(backup_dir, destination)
                print(f"   ✅ {backup_dir} → {destination}")
                moved_count += 1
            except Exception as e:
                print(f"   ❌ 移动失败 {backup_dir}: {e}")
    
    # 生成保留文件清单
    print(f"\n📋 生成文件清单...")
    
    # 扫描当前目录的重要文件
    important_files = {
        "HTML文件": glob.glob("*.html"),
        "CSS文件": glob.glob("*.css"),
        "JavaScript文件": [f for f in glob.glob("*.js") if not f.endswith('dev-tools')],
        "配置文件": ["vercel.json", "redirect-mapping.json"],
        "SEO文件": ["robots.txt", "sitemap.xml"],
        "图标文件": ["*.ico", "*.png", "*.jpg", "*.gif", "*.svg"],
        "其他重要文件": [".gitignore"]
    }
    
    manifest_content = "# 网站文件清单\n"
    manifest_content += f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    total_files = 0
    for category, files in important_files.items():
        if isinstance(files, list) and len(files) > 0:
            # 如果是glob模式，展开文件
            if any('*' in f for f in files):
                expanded_files = []
                for pattern in files:
                    expanded_files.extend(glob.glob(pattern))
                files = expanded_files
            
            # 过滤存在的文件
            existing_files = [f for f in files if os.path.exists(f)]
            
            if existing_files:
                manifest_content += f"## {category} ({len(existing_files)}个)\n"
                for file in sorted(existing_files):
                    file_size = os.path.getsize(file)
                    size_mb = file_size / (1024 * 1024)
                    manifest_content += f"- {file} ({size_mb:.2f}MB)\n"
                manifest_content += "\n"
                total_files += len(existing_files)
    
    manifest_content += f"**总计: {total_files} 个网站文件**\n"
    
    # 保存清单到dev-tools目录
    with open(os.path.join(dev_dir, "website_manifest.md"), 'w', encoding='utf-8') as f:
        f.write(manifest_content)
    
    # 创建部署说明
    deploy_guide = """# 部署指南

## Git提交和推送

```bash
# 1. 查看状态
git status

# 2. 添加重要文件
git add .

# 3. 提交更改
git commit -m "Add Vercel redirect configuration and optimize website"

# 4. 推送到GitHub
git push origin main
```

## Vercel自动部署

推送后，Vercel会自动：
1. 检测到vercel.json配置文件
2. 应用重定向规则
3. 部署网站到全球CDN
4. 生成部署URL

## 验证部署

访问以下URL测试重定向：
- https://yourdomain.vercel.app/jump-run-games
- https://yourdomain.vercel.app/car-games
- https://yourdomain.vercel.app/puzzle-games

## 监控建议

1. 检查Vercel部署日志
2. 监控GSC中404错误变化
3. 验证重定向功能正常工作
"""
    
    with open(os.path.join(dev_dir, "DEPLOY_GUIDE.md"), 'w', encoding='utf-8') as f:
        f.write(deploy_guide)
    
    print(f"✅ 已移动 {moved_count} 个开发文件到 {dev_dir}")
    print(f"📋 生成文件清单: {dev_dir}/website_manifest.md")
    print(f"📖 生成部署指南: {dev_dir}/DEPLOY_GUIDE.md")
    
    # 显示当前目录结构
    print(f"\n📁 当前目录结构:")
    html_files = len(glob.glob("*.html"))
    css_files = len(glob.glob("*.css"))
    js_files = len([f for f in glob.glob("*.js") if f != 'redirect-checker.js'])
    config_files = len([f for f in ["vercel.json", "redirect-mapping.json", ".gitignore"] if os.path.exists(f)])
    
    print(f"   📄 HTML文件: {html_files} 个")
    print(f"   🎨 CSS文件: {css_files} 个") 
    print(f"   ⚙️ 配置文件: {config_files} 个")
    print(f"   🛠️ 开发工具: {dev_dir}/ 目录")
    
    print(f"\n🚀 项目已准备就绪，可以提交到Git!")
    print(f"💡 建议执行命令:")
    print(f"   git add .")
    print(f"   git commit -m 'Add Vercel redirect configuration and clean project'")
    print(f"   git push origin main")

if __name__ == "__main__":
    clean_project()
