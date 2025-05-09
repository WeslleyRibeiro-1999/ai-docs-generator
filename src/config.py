import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME")
    TEMPERATURE = float(os.getenv("TEMPERATURE"))
    PROJECT_PATH = os.getenv("PROJECT_PATH")
    README_PATH = os.getenv("README_PATH")
    NOTION_TOKEN = os.getenv("NOTION_TOKEN")
    NOTION_PAGE_ID = os.getenv("NOTION_PAGE_ID")
    NOTION_API_URL = os.getenv("NOTION_API_URL")
    NOTION_VERSION = os.getenv("NOTION_VERSION")


settings = Settings()
