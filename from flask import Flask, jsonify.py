from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')

def home_page():
    return(f'Welcome to the Homework'
    f'availible routes'
    f'/api/v1.0/precipitation')

if __name__ == '__main__':
    app.run()
    