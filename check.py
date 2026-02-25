# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello from Flask Server!"

# if __name__ == '__main__':
#     app.run(port=8000)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "this is home page"

if __name__ == '__main__':
    app.run(port=7000)