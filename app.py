from flask import Flask, render_template, request
from db import db, Query

# intialize flask app instance.
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    if(request.method == 'POST'):
        # here we check if the person has an account and we 
        # process the information they have entered.
        number = request.form.get('phone')
        pin = request.form.get('pin')
        
        Account = Query()
        if(len(db.search(Account.number == number and Account.pin == pin)) > 0):
            # this means the account exists now we can redirect to the home page
            user = db.search(Account.number == number)
            return render_template('index.html', account=user[0])
            


        return {'pin': pin, 'number': number}


if __name__ == "__main__":
    app.run(debug=True)
