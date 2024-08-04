from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
app.config['DEBUG'] = True


# Replace the URI string with your MongoDB deployment's connection string.
client = MongoClient("mongodb://localhost:27017/")
db = client["rani"]
collection = db["flask1"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    mobile = request.form['mobile']
    password = request.form['password']

    user_data = {
        "name": name,
        "mobile": mobile,
        "password": password
    }

    collection.insert_one(user_data)
    return redirect('/')

if __name__ == '__main__':
    app.run()
