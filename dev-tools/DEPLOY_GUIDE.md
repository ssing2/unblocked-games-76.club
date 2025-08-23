# 部署指南

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
