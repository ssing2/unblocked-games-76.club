import os
import re

# 你的项目根目录
root_dir = r'd:\Web2088\unblocked-games-76.club'

# 选中区footer内容（建议用三引号粘贴完整footer HTML）
new_footer = """
<footer class="text-center footer" id="footer">
    <div class="row footer-nav">
        <div class="col-md-4">
            <h4 class="text-uppercase mb-4">Location</h4>
            <p>1101 Park Clark Garden,<br>MO 0833</p>
        </div>
        <div class="col-md-4">
            <h4 class="text-uppercase mb-4">Friend Sites</h4>
            <div style="font-size: 0.92em;">
                <div class="row">
                    <div class="col-4">
                        <ul class="list-unstyled mb-1">
                            <li><a href="https://areacode.codes" target="_blank" rel="noopener">Area Code Lookup</a></li>
                            <li><a href="https://213area.codes" target="_blank" rel="noopener">213 Area Code</a></li>
                            <li><a href="https://917areacode.org" target="_blank" rel="noopener">917 Area Code</a></li>
                            <li><a href="https://929areacode.net" target="_blank" rel="noopener">929 Area Code</a></li>
                        </ul>
                    </div>
                    <div class="col-4">
                        <ul class="list-unstyled mb-1">
                            <li><a href="https://eggycar.autos" target="_blank" rel="noopener">Eggy Car</a></li>
                            <li><a href="https://slopeunblocked.run" target="_blank" rel="noopener">Slope unblocked</a></li>
                            <li><a href="https://1v1lolunblocked.live" target="_blank" rel="noopener">1v1 lol ynblocked</a></li>
                            <li><a href="https://eggycar.space" target="_blank" rel="noopener">Eggy Car Unblocked</a></li>
                        </ul>
                    </div>
                    <div class="col-4">
                        <ul class="list-unstyled mb-1">
                            <li><a href="https://www.aipinji.com" target="_blank" rel="noopener">aipinji</a></li>
                            <li><a href="https://www.folo.cn" target="_blank" rel="noopener">Folo</a></li>
                            <li><a href="https://www.boxuewu.com" target="_blank" rel="noopener">BoxueWu</a></li>
                            <li><a href="https://bloglines.cn" target="_blank" rel="noopener">Bloglines CN</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <h4 class="text-uppercase">Around the Web</h4>
            <ul class="list-inline">
                <li class="list-inline-item"><a class="btn btn-outline-light text-center btn-social rounded-circle" role="button" href="https://www.facebook.com/Games235/"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icon-tabler-brand-facebook-filled fa-fw"><path stroke="none" d="M0 0h24v24H0z" fill="none"></path><path d="M18 2a1 1 0 0 1 .993 .883l.007 .117v4a1 1 0 0 1 -.883 .993l-.117 .007h-3v1h3a1 1 0 0 1 .991 1.131l-.02 .112l-1 4a1 1 0 0 1 -.858 .75l-.113 .007h-2v6a1 1 0 0 1 -.883 .993l-.117 .007h-4a1 1 0 0 1 -.993 -.883l-.007 -.117v-6h-2a1 1 0 0 1 -.993 -.883l-.007 -.117v-4a1 1 0 0 1 .883 -.993l.117 -.007h2v-1a6 6 0 0 1 5.775 -5.996l.225 -.004h3z" stroke-width="0" fill="currentColor"></path></svg></a></li>
                <li class="list-inline-item"><a class="btn btn-outline-light text-center btn-social rounded-circle" role="button" href="https://www.youtube.com/@ubg235"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icon-tabler-brand-youtube-filled fa-fw"><path stroke="none" d="M0 0h24v24H0z" fill="none"></path><path d="M18 3a5 5 0 0 1 5 5v8a5 5 0 0 1 -5 5h-12a5 5 0 0 1 -5 -5v-8a5 5 0 0 1 5 -5zm-9 6v6a1 1 0 0 0 1.514 .857l5 -3a1 1 0 0 0 0 -1.714l-5 -3a1 1 0 0 0 -1.514 .857z" stroke-width="0" fill="currentColor"></path></svg></a></li>
                <li class="list-inline-item"><a class="btn btn-outline-light text-center btn-social rounded-circle" role="button" href="https://discord.gg/gUeBzA2jaF"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icon-tabler-brand-discord-filled fa-fw"><path stroke="none" d="M0 0h24v24H0z" fill="none"></path><path d="M14.983 3l.123 .006c2.014 .214 3.527 .672 4.966 1.673a1 1 0 0 1 .371 .488c1.876 5.315 2.373 9.987 1.451 12.28c-1.003 2.005 -2.606 3.553 -4.394 3.553c-.732 0 -1.693 -.968 -2.328 -2.045a21.512 21.512 0 0 0 2.103 -.493a1 1 0 1 0 -.55 -1.924c-3.32 .95 -6.13 .95 -9.45 0a1 1 0 0 0 -.55 1.924c.717 .204 1.416 .37 2.103 .494c-.635 1.075 -1.596 2.044 -2.328 2.044c-1.788 0 -3.391 -1.548 -4.428 -3.629c-.888 -2.217 -.39 -6.89 1.485 -12.204a1 1 0 0 1 .371 -.488c1.439 -1.001 2.952 -1.459 4.966 -1.673a1 1 0 0 1 .935 .435l.063 .107l.651 1.285l.137 -.016a12.97 12.97 0 0 1 2.643 0l.134 .016l.65 -1.284a1 1 0 0 1 .754 -.54l.122 -.009zm-5.983 7a2 2 0 0 0 -1.977 1.697l-.018 .154l-.005 .149l.005 .15a2 2 0 1 0 1.995 -2.15zm6 0a2 2 0 0 0 -1.977 1.697l-.018 .154l-.005 .149l.005 .15a2 2 0 1 0 1.995 -2.15z" stroke-width="0" fill="currentColor"></path></svg></a></li>
            </ul>
        </div>
    </div>
    <div class="row copyright">
        <div class="col"><small>Copyright © 2022 - 2025&nbsp;<strong>ubg76</strong> - All Rights Reserved</small></div>
    </div>
</footer>
"""

# 匹配整个<footer ...>...</footer>，支持跨行

footer_pattern = re.compile(r'<footer[\s\S]*?</footer>', re.IGNORECASE)

for dirpath, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.html'):
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            new_content, count = footer_pattern.subn(new_footer, content)
            if count > 0:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Updated footer in: {file_path}')