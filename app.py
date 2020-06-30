import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    color = os.environ.get('COLOR', "green") 
    message = "Welcome !!! This is "+color+" environment" 
    return message

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/Vinodh')
def hello1():
    return 'Krishna'

@app.route('/Bindu')
def hello1():
    return 'Darwaja'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)