import os

def count_files_in_directory(directory):
    """返回目录下所有 Python 文件的数量"""
    return len([f for f in os.listdir(directory) if f.endswith('.py')])

def update_readme():
    """更新 README 文件中的题目数量"""
    easy_count = count_files_in_directory('easy')
    medium_count = count_files_in_directory('medium')
    hard_count = count_files_in_directory('hard')

    readme_content = f"""
# LeetCode Solutions
This repository contains my solutions for LeetCode problems, organized by difficulty and type.

## Structure
- `easy/`: Solutions to easy problems.
- `medium/`: Solutions to medium problems.
- `hard/`: Solutions to hard problems.

## Progress
- Easy: {easy_count} problems
- Medium: {medium_count} problems
- Hard: {hard_count} problems
    """

    # 将更新后的内容写入 README.md 文件
    with open('README.md', 'w') as readme_file:
        readme_file.write(readme_content)

if __name__ == '__main__':
    update_readme()
