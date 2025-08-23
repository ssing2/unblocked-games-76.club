#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分析报错URL并生成重定向解决方案
处理没有.html扩展名的URL到实际.html文件的重定向
"""

import csv
import os
import re
from urllib.parse import urlparse
from collections import defaultdict

def analyze_error_urls():
    csv_file = '报错url.csv'
    
    # 检查CSV文件是否存在
    if not os.path.exists(csv_file):
        print(f"❌ 文件 {csv_file} 不存在")
        return
    
    print("🔍 分析报错URL...")
    print("=" * 60)
    
    # 读取CSV文件，尝试多种编码
    urls_data = []
    encodings = ['utf-8-sig', 'utf-8', 'gbk', 'gb2312', 'latin-1']
    
    for encoding in encodings:
        try:
            with open(csv_file, 'r', encoding=encoding) as f:
                reader = csv.reader(f)
                next(reader)  # 跳过表头
                for row in reader:
                    if len(row) >= 2:
                        url = row[0].strip()
                        date = row[1].strip()
                        urls_data.append((url, date))
            print(f"✅ 成功使用 {encoding} 编码读取CSV文件")
            break
        except Exception as e:
            if encoding == encodings[-1]:  # 最后一个编码也失败了
                print(f"❌ 所有编码都失败了，最后的错误: {e}")
                return
            continue
    
    print(f"📊 总共发现 {len(urls_data)} 个报错URL")
    
    # 分析URL模式
    missing_html_urls = []  # 缺少.html扩展名的URL
    existing_html_urls = []  # 已有.html扩展名的URL
    missing_files = []  # 对应文件不存在的URL
    
    for url, date in urls_data:
        # 解析URL路径
        parsed = urlparse(url)
        path = parsed.path.lstrip('/')  # 移除开头的斜杠
        
        if path.endswith('.html'):
            existing_html_urls.append((path, date))
            # 检查文件是否存在
            if not os.path.exists(path):
                missing_files.append((path, date))
        else:
            missing_html_urls.append((path, date))
            # 检查对应的.html文件是否存在
            html_file = f"{path}.html"
            if os.path.exists(html_file):
                missing_html_urls[-1] = (path, date, html_file)  # 添加对应的html文件名
    
    print(f"\n📋 URL分类统计:")
    print(f"   缺少.html扩展名: {len(missing_html_urls)} 个")
    print(f"   已有.html扩展名: {len(existing_html_urls)} 个")
    print(f"   对应文件不存在: {len(missing_files)} 个")
    
    # 分析需要重定向的URL
    redirect_rules = []
    for item in missing_html_urls:
        if len(item) == 3:  # 有对应的html文件
            path, date, html_file = item
            redirect_rules.append((path, html_file))
    
    print(f"\n🔄 需要创建重定向规则: {len(redirect_rules)} 个")
    
    # 生成.htaccess重定向规则
    generate_htaccess_rules(redirect_rules)
    
    # 生成Nginx重定向规则
    generate_nginx_rules(redirect_rules)
    
    # 生成HTML重定向页面
    generate_html_redirects(redirect_rules)
    
    # 生成缺失文件报告
    if missing_files:
        generate_missing_files_report(missing_files)
    
    print(f"\n✅ 分析完成!")
    print(f"📁 生成的文件:")
    print(f"   - redirect_rules.htaccess (Apache重定向规则)")
    print(f"   - redirect_rules.nginx (Nginx重定向规则)")
    print(f"   - html_redirects/ (HTML重定向页面)")
    if missing_files:
        print(f"   - missing_files_report.txt (缺失文件报告)")

def generate_htaccess_rules(redirect_rules):
    """生成Apache .htaccess重定向规则"""
    content = """# Apache重定向规则
# 将没有.html扩展名的URL重定向到对应的.html文件
# 使用301永久重定向确保SEO权重传递

RewriteEngine On

# 重定向规则 - 没有.html扩展名的URL到.html文件
"""
    
    for path, html_file in redirect_rules:
        # 转义特殊字符
        escaped_path = re.escape(path)
        content += f"RewriteRule ^{escaped_path}$ /{html_file} [R=301,L]\n"
    
    content += """
# 通用规则：如果请求的文件不存在，但对应的.html文件存在，则重定向
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME}.html -f
RewriteRule ^(.*)$ $1.html [R=301,L]
"""
    
    with open('redirect_rules.htaccess', 'w', encoding='utf-8') as f:
        f.write(content)

def generate_nginx_rules(redirect_rules):
    """生成Nginx重定向规则"""
    content = """# Nginx重定向规则
# 将没有.html扩展名的URL重定向到对应的.html文件
# 使用301永久重定向确保SEO权重传递

"""
    
    for path, html_file in redirect_rules:
        content += f"rewrite ^/{path}$ /{html_file} permanent;\n"
    
    content += """
# 通用规则：如果请求的文件不存在，但对应的.html文件存在，则重定向
location / {
    try_files $uri $uri.html $uri/ @redirect;
}

location @redirect {
    rewrite ^/(.*)$ /$1.html permanent;
}
"""
    
    with open('redirect_rules.nginx', 'w', encoding='utf-8') as f:
        f.write(content)

def generate_html_redirects(redirect_rules):
    """生成HTML重定向页面"""
    # 创建重定向页面目录
    os.makedirs('html_redirects', exist_ok=True)
    
    for path, html_file in redirect_rules:
        # 创建HTML重定向页面
        redirect_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redirecting...</title>
    <meta http-equiv="refresh" content="0; url=/{html_file}">
    <link rel="canonical" href="/{html_file}">
    <script>
        // JavaScript重定向（备用方案）
        window.location.replace('/{html_file}');
    </script>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background-color: #f0f2f5;
        }}
        .redirect-message {{
            max-width: 600px;
            margin: 0 auto;
            padding: 30px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .spinner {{
            border: 4px solid #f3f3f3;
            border-top: 4px solid #007bff;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 20px auto;
        }}
        @keyframes spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
    </style>
</head>
<body>
    <div class="redirect-message">
        <h1>Redirecting...</h1>
        <div class="spinner"></div>
        <p>You are being redirected to the correct page.</p>
        <p>If you are not redirected automatically, <a href="/{html_file}">click here</a>.</p>
    </div>
</body>
</html>"""
        
        # 保存重定向页面
        redirect_file = f"html_redirects/{path.replace('/', '_')}.html"
        with open(redirect_file, 'w', encoding='utf-8') as f:
            f.write(redirect_content)

def generate_missing_files_report(missing_files):
    """生成缺失文件报告"""
    content = "缺失文件报告\n"
    content += "=" * 50 + "\n"
    content += f"生成时间: {os.popen('date /t').read().strip()}\n\n"
    
    content += "以下文件被外部链接引用但在服务器上不存在:\n\n"
    
    for file_path, date in missing_files:
        content += f"文件: {file_path}\n"
        content += f"最后抓取: {date}\n"
        content += f"建议: 创建该文件或设置重定向\n"
        content += "-" * 30 + "\n"
    
    with open('missing_files_report.txt', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    analyze_error_urls()
