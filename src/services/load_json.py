import json
import os

# Get the directory containing this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

class AccountsManager:
    _accounts = None

    @classmethod
    def _load_accounts(cls):
        if cls._accounts is None:
            json_path = os.path.join(os.path.dirname(os.path.dirname(SCRIPT_DIR)), 'cat_cuentas.json')
            with open(json_path, 'r') as jsonfile:
                cls._accounts = json.load(jsonfile)

    @classmethod
    def get_account(cls, account_id):
        cls._load_accounts()
        return cls._accounts.get(account_id)

    @classmethod
    def get_accounts(cls):
        cls._load_accounts()
        return cls._accounts

