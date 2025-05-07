from flask import Flask,url_for,redirect

app = Flask(__name__,static_url_path='',static_folder='../static') #template_folder='templates'

@app.route('/')

def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)