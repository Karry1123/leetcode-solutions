name: Update README Progress

# 触发条件：当推送到 main 分支时，或手动触发
on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  update-readme:
    runs-on: ubuntu-latest

    steps:
      # 检出代码库
      - name: Checkout repository
        uses: actions/checkout@v3

      # 设置 Python 环境
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      # 安装必要依赖（如果有 requirements.txt，可扩展此步骤）
      - name: Install dependencies
        run: pip install -r requirements.txt || true

      # 运行 Python 脚本更新 README.md
      - name: Update README.md
        run: python update_readme.py

      # 提交更改到 GitHub
      - name: Commit and push changes
        run: |
          git config --global user.name "GitHub Actions Bot"
          git config --global user.email "actions@github.com"
          git add README.md
          git commit -m "Update problem count in README"
          git push
