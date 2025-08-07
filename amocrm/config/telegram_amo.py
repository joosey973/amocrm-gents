from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
    AMOCRM_TOKEN = os.environ.get('AMOCRM_TOKEN')


config = Config()
