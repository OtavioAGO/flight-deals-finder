import os
from requests_cache import CachedSession
from dotenv import load_dotenv

load_dotenv()
class DataManager:
    def __init__(self):
        self.url = os.getenv('SHEETY_URL')
        self.header = {'Authorization':f"Bearer {os.getenv('SHEETY_TOKEN')}"}
        self.session = CachedSession('data_cache')

    def get_data(self):
        res = self.session.get(self.url, self.header)
        return res.json()
    