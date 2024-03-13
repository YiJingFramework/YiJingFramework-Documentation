extensions = ["nbsphinx", "sphinx_favicon"]

templates_path = []
exclude_patterns = []
html_static_path = ["wwwroot"]

project = "YiJingFramework"
language = 'zh_CN'

html_theme = "sphinx_book_theme"
html_theme_options = {
    "extra_footer": "这里是 YiJingFramework 的文档。前往 "
                    "<a href=\"https://yjfwk.yueyinqiu.top/\">https://yjfwk.yueyinqiu.top/</a> "
                    "查看更多项目。"
}
# html_logo = "taiji.png"
html_title = "YiJingFramework"
favicons = [
    {
        "href": "taiji.png" 
    },
]

nbsphinx_codecell_lexer = "csharp"
pygments_style = "vs"
nbsphinx_execute = "never"