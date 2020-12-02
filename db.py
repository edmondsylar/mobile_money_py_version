from tinydb import TinyDB, Query # importing our database here.

db = TinyDB('accounts.json')
# here lets generate a test account 
#  lets first make sure there is no record that macteches the one we are going to create.

def __init():
    Acc = Query()
    found = db.search(Acc.number == '0701207194')

    if(len(found) == 0):
        # lets create the account now
        db.insert(
            {'number': '0701207194', 'pin': '1111', 'balance': 200000}
        )
    return True




__init()