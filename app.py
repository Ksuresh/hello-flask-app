from flask import Flask

app = Flask(__name__)
API_KEY = "AKIAFAKEKEY123456789"
@app.route('/')
def hello():
    return "Hello, Suresh! DevSecOps Demo is Working 🎉"

if __name__ == '__main__':
    app.run(debug=True)
