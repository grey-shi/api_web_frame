import os, json
root_path = os.path.dirname(__file__)
root_path = os.path.dirname(root_path)

def login_json():
    with open(root_path + '\\login.json', 'r', encoding='utf-8-sig') as f:
        login_data = json.load(f)
    return login_data
