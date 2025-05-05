import os


def write_readme_file(content: str, directory: str, filename: str = "README.md") -> None:
    os.makedirs(directory, exist_ok=True)

    file_path = os.path.join(directory, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
