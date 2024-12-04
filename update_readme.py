import os

# 定义文件夹路径
easy_dir = 'easy'
medium_dir = 'medium'
hard_dir = 'hard'

# 统计文件夹中的题目数量
def count_problems(directory):
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

# 获取各个文件夹中的题目数量
easy_count = count_problems(easy_dir)
medium_count = count_problems(medium_dir)
hard_count = count_problems(hard_dir)

# 更新README.md文件中的进度
def update_readme():
    # 读取当前README文件
    with open('README.md', 'r', encoding='utf-8') as file:
        content = file.read()

    # 构建新的进度部分
    progress_section = f"## Progress\n- Easy: {easy_count} problems\n- Medium: {medium_count} problems\n- Hard: {hard_count} problems\n"
    
    # 检查README中是否已经有Progress部分，如果有就替换它
    if '## Progress' in content:
        start = content.find('## Progress')
        end = content.find('##', start + 1)
        if end == -1:
            content = content[:start] + progress_section
        else:
            content = content[:start] + progress_section + content[end:]
    else:
        # 如果没有Progress部分，就在末尾添加它
        content += "\n" + progress_section

    # 写回更新后的README文件
    with open('README.md', 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    update_readme()
