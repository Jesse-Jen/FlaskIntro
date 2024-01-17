from flask import Flask
app = Flask(__name__)

@app.route('/welcome', methods = ['GET'])
def welcome():
    return 'Welcome'

@app.route('/welcome/home', methods = ['GET'])
def welcome_home():
    return 'welcome home'

@app.route('/welcome/back', methods = ['GET'])
def welcome_back():
    return 'welcome back'



if __name__ == '__main__':
    app.run(debug = True)