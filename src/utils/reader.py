import os


def read_code_from_directory(directory_path: str) -> list:
    project_files = []

    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, encoding="utf-8") as f:
                        content = f.read()
                    project_files.append((file_path, content))
                except Exception as e:
                    print(f"[ERRO] Falha ao ler {file_path}: {e}")

    return project_files
