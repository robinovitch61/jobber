import requests
import subprocess

lists = requests.get("https://api.trello.com/1/boards/eOMM0F9O/lists")
lists.raise_for_status()
list_data = lists.json()

#[{'id': '62d608c8813cfa14a47a81a5', 'name': 'Introduction', 'closed': False, 'idBoard': '62cca86be4387e712693e9eb', 'pos': 2048, 'subscribed': None, 'softLimit': None}, {'id': '62cca86be4387e712693e9f3', 'name': 'Puppies', 'closed': False, 'idBoard': '62cca86be4387e712693e9eb', 'pos': 7680, 'subscribed': None, 'softLimit': None}, {'id': '62ccaf8b56d84d53dcb5bb6c', 'name': 'Respite Foster Dogs', 'closed': False, 'idBoard': '62cca86be4387e712693e9eb', 'pos': 11904, 'subscribed': None, 'softLimit': None}, {'id': '62ccad6c61db851845449f9b', 'name': 'Nursing Queen', 'closed': False, 'idBoard': '62cca86be4387e712693e9eb', 'pos': 16128, 'subscribed': None, 'softLimit': None}, {'id': '62cca86be4387e712693e9f4', 'name': 'Adult Cat', 'closed': False, 'idBoard': '62cca86be4387e712693e9eb', 'pos': 22464, 'subscribed': None, 'softLimit': None}, {'id': '62ccad6e7fd1878cce4ecdcb', 'name': 'Nursing Bees', 'closed': False, 'idBoard': '62cca86be4387e712693e9eb', 'pos': 24576, 'subscribed': None, 'softLimit': None}, {'id': '62cca86be4387e712693e9f2', 'name': 'Kittens (remember to scroll down!)', 'closed': False, 'idBoard': '62cca86be4387e712693e9eb', 'pos': 29696, 'subscribed': None, 'softLimit': None}, {'id': '62cca89368b61564309b7094', 'name': 'Adult Dog', 'closed': False, 'idBoard': '62cca86be4387e712693e9eb', 'pos': 43008, 'subscribed': None, 'softLimit': None}]

adult_list_id = [l for l in list_data if "adultcat" in l["name"].replace(" ","").lower()][0]["id"]
print(adult_list_id)

cards = requests.get(f"https://api.trello.com/1/lists/{adult_list_id}/cards")
cards.raise_for_status()
card_data = cards.json()
print(card_data)

if len(card_data):
    applescript = """
    display dialog "there are cats" ¬
    with title "THERE ARE CATS" ¬
    with icon caution ¬
    buttons {"OK"}
    """

    subprocess.call("osascript -e '{}'".format(applescript), shell=True)
