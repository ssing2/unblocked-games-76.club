#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证Vercel配置文件
确保所有重定向规则正确配置
"""

import json
import os

def verify_vercel_config():
    print("🔍 验证Vercel配置...")
    print("=" * 50)
    
    # 检查vercel.json是否存在
    if not os.path.exists('vercel.json'):
        print("❌ vercel.json 文件不存在！")
        return False
    
    try:
        with open('vercel.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ vercel.json 格式错误: {e}")
        return False
    except Exception as e:
        print(f"❌ 读取 vercel.json 失败: {e}")
        return False
    
    print("✅ vercel.json 文件格式正确")
    
    # 验证配置结构
    if 'redirects' not in config:
        print("❌ 缺少 redirects 配置")
        return False
    
    if 'errorPage' not in config:
        print("⚠️  建议添加 errorPage 配置")
    else:
        print(f"✅ 404错误页面: {config['errorPage']}")
    
    # 验证重定向规则
    redirects = config['redirects']
    print(f"\n📋 重定向规则分析:")
    print(f"   规则数量: {len(redirects)}")
    
    # 检查规则格式
    valid_rules = 0
    invalid_rules = 0
    missing_files = []
    
    for i, rule in enumerate(redirects):
        # 检查必需字段
        if 'source' not in rule or 'destination' not in rule:
            print(f"❌ 规则 {i+1}: 缺少 source 或 destination")
            invalid_rules += 1
            continue
        
        # 检查permanent字段
        if 'permanent' not in rule or rule['permanent'] != True:
            print(f"⚠️  规则 {i+1}: 建议设置 permanent: true")
        
        # 检查目标文件是否存在
        destination = rule['destination'].lstrip('/')
        if not os.path.exists(destination):
            missing_files.append(destination)
        
        valid_rules += 1
    
    print(f"   有效规则: {valid_rules}")
    print(f"   无效规则: {invalid_rules}")
    
    # 检查目标文件
    if missing_files:
        print(f"\n⚠️  {len(missing_files)} 个目标文件不存在:")
        for file in missing_files[:10]:  # 只显示前10个
            print(f"      - {file}")
    else:
        print("✅ 所有重定向目标文件都存在")
    
    # 验证与redirect-mapping.json的一致性
    if os.path.exists('redirect-mapping.json'):
        print(f"\n🔄 与重定向映射文件对比:")
        with open('redirect-mapping.json', 'r', encoding='utf-8') as f:
            mapping = json.load(f)
        
        vercel_sources = {rule['source'].lstrip('/') for rule in redirects}
        mapping_sources = set(mapping.keys())
        
        only_in_vercel = vercel_sources - mapping_sources
        only_in_mapping = mapping_sources - vercel_sources
        
        print(f"   映射文件规则: {len(mapping_sources)}")
        print(f"   Vercel规则: {len(vercel_sources)}")
        print(f"   仅在Vercel中: {len(only_in_vercel)}")
        print(f"   仅在映射中: {len(only_in_mapping)}")
        
        if only_in_mapping:
            print(f"   建议添加到Vercel: {list(only_in_mapping)[:5]}")
    
    # 检查常见的Vercel配置问题
    print(f"\n🔧 Vercel最佳实践检查:")
    
    # 检查source路径格式
    sources_without_slash = [rule['source'] for rule in redirects if not rule['source'].startswith('/')]
    if sources_without_slash:
        print(f"⚠️  {len(sources_without_slash)} 个source路径没有以/开头")
    else:
        print("✅ 所有source路径格式正确")
    
    # 检查destination路径格式
    destinations_without_slash = [rule['destination'] for rule in redirects if not rule['destination'].startswith('/')]
    if destinations_without_slash:
        print(f"⚠️  {len(destinations_without_slash)} 个destination路径没有以/开头")
    else:
        print("✅ 所有destination路径格式正确")
    
    # 检查是否有重复的source
    sources = [rule['source'] for rule in redirects]
    duplicates = set([x for x in sources if sources.count(x) > 1])
    if duplicates:
        print(f"❌ 发现重复的source路径: {duplicates}")
    else:
        print("✅ 没有重复的重定向规则")
    
    # 生成部署命令
    print(f"\n🚀 Vercel部署命令:")
    print("   git add vercel.json 404.html redirect-mapping.json")
    print("   git commit -m 'Add Vercel redirect configuration'")
    print("   git push origin main")
    print("   # Vercel会自动重新部署")
    
    # 生成测试URL
    print(f"\n🧪 测试URL示例:")
    sample_rules = redirects[:3]  # 取前3个规则作为示例
    for rule in sample_rules:
        source = rule['source']
        destination = rule['destination']
        print(f"   访问: https://yourdomain.vercel.app{source}")
        print(f"   期望: 301重定向到 {destination}")
        print()
    
    # 总体评分
    score = 0
    max_score = 6
    
    if len(redirects) > 50: score += 1
    if invalid_rules == 0: score += 1
    if len(missing_files) == 0: score += 1
    if len(sources_without_slash) == 0: score += 1
    if len(destinations_without_slash) == 0: score += 1
    if len(duplicates) == 0: score += 1
    
    percentage = (score / max_score) * 100
    
    if percentage >= 90:
        grade = "🏆 优秀 - 配置完美"
    elif percentage >= 80:
        grade = "🥈 良好 - 配置基本正确"
    elif percentage >= 70:
        grade = "🥉 中等 - 需要小幅调整"
    else:
        grade = "⚠️  需要修复配置问题"
    
    print(f"📊 配置评分: {score}/{max_score} ({percentage:.0f}%)")
    print(f"🏆 评级: {grade}")
    
    return score >= 5

if __name__ == "__main__":
    success = verify_vercel_config()
    if success:
        print("\n✅ Vercel配置验证通过，可以部署！")
    else:
        print("\n❌ 请修复配置问题后再部署")
