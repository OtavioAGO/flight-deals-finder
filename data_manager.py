import os
from requests_cache import CachedSession


class DataManager:
    def __init__(self):
        self.url = os.getenv('SHEETY_URL')
        self.header = {'Authorization':f"Bearer {os.getenv('SHEETY_TOKEN')}"}
        self.session = CachedSession('data_cache')

    def get_data(self):
        res = self.session.get(self.url, self.header)
        return res.json()

    def update_data(self, row_id, new_price):
        new_data = {
            "ticket": {
                "lowestPrice" : new_price
            }
        }
        res = self.session.put(url=f"{self.url}/{row_id}", json= new_data, headers = self.header)
        return res.text