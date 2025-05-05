import requests
from config import settings


def split_into_blocks(text, limit=2000):
    blocks = []
    current = ""

    for line in text.split("\n"):
        if len(current) + len(line) + 1 <= limit:
            current += line + "\n"
        else:
            blocks.append(current.strip())
            current = line + "\n"

    if current.strip():
        blocks.append(current.strip())

    return blocks


def append_to_notion_page(content):
    blocks = split_into_blocks(content)

    children = [
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {"rich_text": [{"type": "text", "text": {"content": block}}]},
        }
        for block in blocks
    ]

    url = f"https://api.notion.com/v1/blocks/{settings.NOTION_PAGE_ID}/children"

    headers = {
        "Authorization": f"Bearer {settings.NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": settings.NOTION_VERSION,
    }

    response = requests.patch(url, headers=headers, json={"children": children})

    if response.status_code == 200:
        print("Conteúdo adicionado com sucesso!")
    else:
        print(f"Erro {response.status_code}: {response.text}")
