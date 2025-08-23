#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
创建通用的404错误处理页面和JavaScript重定向解决方案
这是最实用的解决方案，不需要服务器配置
"""

import os
import json

def create_404_redirect_solution():
    print("🔧 创建404重定向解决方案...")
    
    # 1. 创建404错误页面
    create_404_page()
    
    # 2. 创建重定向映射JSON文件
    create_redirect_mapping()
    
    # 3. 创建通用重定向脚本
    create_redirect_script()
    
    print("✅ 404重定向解决方案创建完成!")

def create_404_page():
    """创建智能404错误页面"""
    content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found - Unblocked Games 76</title>
    <meta name="description" content="The page you're looking for might have moved. We'll try to redirect you to the correct page automatically.">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }
        
        .container {
            text-align: center;
            max-width: 600px;
            padding: 2rem;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        
        .error-code {
            font-size: 6rem;
            font-weight: bold;
            margin-bottom: 1rem;
            background: linear-gradient(45deg, #ff6b6b, #feca57);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .error-message {
            font-size: 1.5rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }
        
        .redirect-info {
            background: rgba(255, 255, 255, 0.1);
            padding: 1.5rem;
            border-radius: 10px;
            margin: 2rem 0;
            display: none;
        }
        
        .redirect-info.show {
            display: block;
        }
        
        .spinner {
            border: 3px solid rgba(255, 255, 255, 0.3);
            border-top: 3px solid white;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 1rem auto;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .btn {
            display: inline-block;
            padding: 12px 24px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            text-decoration: none;
            border-radius: 25px;
            margin: 0.5rem;
            transition: transform 0.3s ease;
        }
        
        .btn:hover {
            transform: translateY(-2px);
        }
        
        .suggestions {
            margin-top: 2rem;
            text-align: left;
        }
        
        .suggestions h3 {
            margin-bottom: 1rem;
            text-align: center;
        }
        
        .suggestion-list {
            list-style: none;
            padding: 0;
        }
        
        .suggestion-list li {
            margin: 0.5rem 0;
            padding: 0.5rem;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 5px;
        }
        
        .suggestion-list a {
            color: #feca57;
            text-decoration: none;
        }
        
        .suggestion-list a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="error-code">404</div>
        <div class="error-message">Oops! Page not found</div>
        
        <div class="redirect-info" id="redirectInfo">
            <div class="spinner"></div>
            <p>We found a matching page! Redirecting you in <span id="countdown">5</span> seconds...</p>
            <p><a href="#" id="redirectLink" class="btn">Go Now</a></p>
        </div>
        
        <div id="noRedirect">
            <p>The page you're looking for might have moved or no longer exists.</p>
            
            <div style="margin: 2rem 0;">
                <a href="/" class="btn">🏠 Home</a>
                <a href="/car-games.html" class="btn">🚗 Car Games</a>
                <a href="/puzzle-games.html" class="btn">🧩 Puzzle Games</a>
                <a href="/sports-games.html" class="btn">⚽ Sports Games</a>
            </div>
        </div>
        
        <div class="suggestions" id="suggestions" style="display: none;">
            <h3>Did you mean one of these?</h3>
            <ul class="suggestion-list" id="suggestionList">
                <!-- 动态生成建议 -->
            </ul>
        </div>
    </div>

    <script>
        // 重定向映射和逻辑
        const redirectMap = {
            // 这个映射会通过JavaScript动态加载
        };
        
        // 智能重定向函数
        function smartRedirect() {
            const currentPath = window.location.pathname;
            const pathWithoutSlash = currentPath.replace(/^\//, '');
            
            // 检查是否需要添加.html扩展名
            const possiblePaths = [
                pathWithoutSlash + '.html',
                pathWithoutSlash,
                pathWithoutSlash.replace(/\/$/, '.html')
            ];
            
            // 加载重定向映射
            loadRedirectMapping().then(mapping => {
                let targetUrl = null;
                
                for (const path of possiblePaths) {
                    if (mapping[path] || mapping['/' + path]) {
                        targetUrl = mapping[path] || mapping['/' + path];
                        break;
                    }
                }
                
                // 如果没有找到映射，尝试直接添加.html
                if (!targetUrl && !pathWithoutSlash.endsWith('.html')) {
                    targetUrl = pathWithoutSlash + '.html';
                }
                
                if (targetUrl) {
                    showRedirectInfo(targetUrl);
                } else {
                    showSuggestions(pathWithoutSlash, mapping);
                }
            });
        }
        
        // 加载重定向映射
        async function loadRedirectMapping() {
            try {
                const response = await fetch('/redirect-mapping.json');
                if (response.ok) {
                    return await response.json();
                }
            } catch (error) {
                console.log('No redirect mapping found');
            }
            
            // 如果没有映射文件，返回基本映射
            return getBasicMapping();
        }
        
        // 基本映射（从分析结果生成）
        function getBasicMapping() {
            return {
                'jump-run-games': 'jump-run-games.html',
                'car-games': 'car-games.html',
                'sports-games': 'sports-games.html',
                'shooting-games': 'shooting-games.html',
                'puzzle-games': 'puzzle-games.html',
                'idle-games': 'idle-games.html',
                'adventure-games': 'adventure-games.html',
                'survival-games': 'survival-games.html',
                'merge-games': 'merge-games.html',
                'throwing-games': 'throwing-games.html',
                'restaurant-games': 'restaurant-games.html',
                'simulator-games': 'simulator-games.html',
                'fighting-games': 'fighting-games.html',
                'word-games': 'word-games.html',
                'music-games': 'music-games.html',
                'bus-games': 'bus-games.html',
                'clicker-games': 'clicker-games.html',
                'cards-games': 'cards-games.html',
                'tower-defense-games': 'tower-defense-games.html',
                'truck-games': 'truck-games.html'
            };
        }
        
        // 显示重定向信息
        function showRedirectInfo(targetUrl) {
            const redirectInfo = document.getElementById('redirectInfo');
            const redirectLink = document.getElementById('redirectLink');
            const noRedirect = document.getElementById('noRedirect');
            
            redirectLink.href = '/' + targetUrl;
            redirectInfo.classList.add('show');
            noRedirect.style.display = 'none';
            
            // 倒计时重定向
            let countdown = 5;
            const countdownElement = document.getElementById('countdown');
            
            const timer = setInterval(() => {
                countdown--;
                countdownElement.textContent = countdown;
                
                if (countdown <= 0) {
                    clearInterval(timer);
                    window.location.href = '/' + targetUrl;
                }
            }, 1000);
        }
        
        // 显示建议
        function showSuggestions(searchPath, mapping) {
            const suggestions = document.getElementById('suggestions');
            const suggestionList = document.getElementById('suggestionList');
            
            // 查找相似的路径
            const similarPaths = findSimilarPaths(searchPath, Object.keys(mapping));
            
            if (similarPaths.length > 0) {
                suggestionList.innerHTML = '';
                similarPaths.slice(0, 5).forEach(path => {
                    const li = document.createElement('li');
                    li.innerHTML = `<a href="/${mapping[path]}">${path.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</a>`;
                    suggestionList.appendChild(li);
                });
                suggestions.style.display = 'block';
            }
        }
        
        // 查找相似路径
        function findSimilarPaths(searchPath, paths) {
            const searchWords = searchPath.toLowerCase().split(/[-_]/);
            
            return paths
                .map(path => ({
                    path: path,
                    score: calculateSimilarity(searchWords, path.toLowerCase().split(/[-_]/))
                }))
                .filter(item => item.score > 0)
                .sort((a, b) => b.score - a.score)
                .map(item => item.path);
        }
        
        // 计算相似度
        function calculateSimilarity(words1, words2) {
            let score = 0;
            for (const word1 of words1) {
                for (const word2 of words2) {
                    if (word1.includes(word2) || word2.includes(word1)) {
                        score++;
                    }
                }
            }
            return score;
        }
        
        // 页面加载时执行
        document.addEventListener('DOMContentLoaded', smartRedirect);
    </script>
</body>
</html>'''
    
    with open('404.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 创建了智能404页面: 404.html")

def create_redirect_mapping():
    """创建重定向映射JSON文件"""
    # 基于CSV分析结果创建映射
    mapping = {
        'jump-run-games': 'jump-run-games.html',
        'car-games': 'car-games.html',
        'sports-games': 'sports-games.html',
        'shooting-games': 'shooting-games.html',
        'puzzle-games': 'puzzle-games.html',
        'idle-games': 'idle-games.html',
        'adventure-games': 'adventure-games.html',
        'survival-games': 'survival-games.html',
        'merge-games': 'merge-games.html',
        'throwing-games': 'throwing-games.html',
        'restaurant-games': 'restaurant-games.html',
        'simulator-games': 'simulator-games.html',
        'fighting-games': 'fighting-games.html',
        'word-games': 'word-games.html',
        'music-games': 'music-games.html',
        'bus-games': 'bus-games.html',
        'clicker-games': 'clicker-games.html',
        'cards-games': 'cards-games.html',
        'tower-defense-games': 'tower-defense-games.html',
        'truck-games': 'truck-games.html',
        
        # 游戏页面映射
        'heads-arena-soccer-all-stars-unblocked': 'heads-arena-soccer-all-stars-unblocked.html',
        'geometry-jump-unblocked': 'geometry-jump-unblocked.html',
        'hanger-unblocked': 'hanger-unblocked.html',
        'super-mario-wonder-unblocked': 'super-mario-wonder-unblocked.html',
        'roper-unblocked': 'roper-unblocked.html',
        'apple-shooter-unblocked': 'apple-shooter-unblocked.html',
        'basket-and-ball-unblocked': 'basket-and-ball-unblocked.html',
        '3d-bowling-unblocked': '3d-bowling-unblocked.html',
        'basketball-legends-2020-unblocked': 'basketball-legends-2020-unblocked.html',
        'bubble-pop-adventures-unblocked': 'bubble-pop-adventures-unblocked.html',
        '3-pandas-in-japan-unblocked': '3-pandas-in-japan-unblocked.html',
        'mr-bullet-unblocked': 'mr-bullet-unblocked.html',
        'basketball-line-unblocked': 'basketball-line-unblocked.html',
        'little-alchemy-2-unblocked': 'little-alchemy-2-unblocked.html',
        'biker-street-unblocked': 'biker-street-unblocked.html',
        'head-soccer-2023-unblocked': 'head-soccer-2023-unblocked.html',
        'eggy-car-unblocked': 'eggy-car-unblocked.html',
        'ball-sort-soccer-unblocked': 'ball-sort-soccer-unblocked.html',
        'dead-again-unblocked': 'dead-again-unblocked.html',
        'ball-sort-puzzle-unblocked': 'ball-sort-puzzle-unblocked.html',
        'rusher-crusher-unblocked': 'rusher-crusher-unblocked.html',
        'bob-the-robber-2-unblocked': 'bob-the-robber-2-unblocked.html',
        'car-rush-unblocked': 'car-rush-unblocked.html',
        'adam-and-eve-7-unblocked': 'adam-and-eve-7-unblocked.html',
        'bouncy-woods-unblocked': 'bouncy-woods-unblocked.html',
        'boxing-random-unblocked': 'boxing-random-unblocked.html',
        'chicken-merge-unblocked': 'chicken-merge-unblocked.html',
        'ball-sort-halloween-unblocked': 'ball-sort-halloween-unblocked.html',
        'doodle-jump-unblocked': 'doodle-jump-unblocked.html',
        'adventure-drivers-unblocked': 'adventure-drivers-unblocked.html',
        'papa-cherry-saga-unblocked': 'papa-cherry-saga-unblocked.html',
        'fruit-ninja-unblocked': 'fruit-ninja-unblocked.html',
        'marbles-sorting-unblocked': 'marbles-sorting-unblocked.html',
        'infinite-soccer-unblocked': 'infinite-soccer-unblocked.html',
        'age-of-war-unblocked': 'age-of-war-unblocked.html'
    }
    
    with open('redirect-mapping.json', 'w', encoding='utf-8') as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)
    
    print("✅ 创建了重定向映射文件: redirect-mapping.json")

def create_redirect_script():
    """创建通用重定向检测脚本"""
    script_content = '''// 通用重定向检测脚本
// 可以插入到其他页面中，自动检测并建议正确的URL

(function() {
    'use strict';
    
    // 检查当前URL是否需要重定向
    function checkForRedirect() {
        const currentPath = window.location.pathname;
        
        // 如果已经是正确的.html路径，无需处理
        if (currentPath.endsWith('.html')) {
            return;
        }
        
        // 尝试添加.html扩展名
        const htmlPath = currentPath.endsWith('/') ? 
            currentPath.slice(0, -1) + '.html' : 
            currentPath + '.html';
        
        // 检查正确的路径是否存在
        fetch(htmlPath, { method: 'HEAD' })
            .then(response => {
                if (response.ok) {
                    // 如果存在，提示用户或自动重定向
                    if (confirm(`This page has moved to ${htmlPath}. Would you like to go there now?`)) {
                        window.location.href = htmlPath;
                    }
                }
            })
            .catch(() => {
                // 静默处理错误
            });
    }
    
    // 页面加载完成后检查
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', checkForRedirect);
    } else {
        checkForRedirect();
    }
})();'''
    
    with open('redirect-checker.js', 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    print("✅ 创建了重定向检测脚本: redirect-checker.js")

if __name__ == "__main__":
    create_404_redirect_solution()
