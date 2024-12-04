import os

def count_problems():
    """统计各难度文件夹中的文件数量"""
    folders = {"easy": "easy", "medium": "medium", "hard": "hard"}
    counts = {}
    for difficulty, folder in folders.items():
        counts[difficulty] = len([f for f in os.listdir(folder) if f.endswith('.py')])
    return counts

def update_readme(counts):
    """更新 README.md 文件的 Progress 部分"""
    readme_path = "README.md"
    with open(readme_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(readme_path, "w", encoding="utf-8") as file:
        for line in lines:
            if line.startswith("- **Easy**:"):
                file.write(f"- **Easy**: {counts['easy']} problems\n")
            elif line.startswith("- **Medium**:"):
                file.write(f"- **Medium**: {counts['medium']} problems\n")
            elif line.startswith("- **Hard**:"):
                file.write(f"- **Hard**: {counts['hard']} problems\n")
            else:
                file.write(line)

if __name__ == "__main__":
    counts = count_problems()
    update_readme(counts)
    print(f"Updated README.md with counts: {counts}")
