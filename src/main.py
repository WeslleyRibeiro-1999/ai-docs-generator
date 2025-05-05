from config import settings
from core.generator import documentation_generator
from utils.reader import read_code_from_directory
from utils.writer import write_readme_file


def main():
    code = read_code_from_directory(settings.PROJECT_PATH)
    dev_doc, biz_doc = documentation_generator(code)
    write_readme_file(dev_doc, settings.README_PATH, "DEVDOC.md")
    write_readme_file(biz_doc, settings.README_PATH, "BIZDOC.md")
    print(f"README.md atualizado com sucesso em: {settings.README_PATH}")


if __name__ == "__main__":
    main()
