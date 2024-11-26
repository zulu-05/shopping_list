import json
import os


class DataManager:

    DATA_FILE = os.path.join('data', 'shopping_lists.json')


    def save_data(self, data):

        with open(self.DATA_FILE, 'w') as f:
            json.dump(data, f)


    def load_data(self):

        try:
            with open(self.DATA_FILE, 'r') as f:
                return json.load(f)

        except FileNotFoundError:
            return {}



