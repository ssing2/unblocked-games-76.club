// 通用重定向检测脚本
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
})();