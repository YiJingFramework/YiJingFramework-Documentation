extensions = ["nbsphinx"]

templates_path = []
exclude_patterns = []
html_static_path = []

project = "YiJingFramework"
language = 'zh_CN'

html_theme = "sphinx_book_theme"
html_theme_options = {
    "extra_footer": "这里是 YiJingFramework 的文档。",
}
# html_logo = "taiji32.png"
html_title = "YiJingFramework"

nbsphinx_codecell_lexer = "csharp"
pygments_style = "vs"
nbsphinx_execute = "never"