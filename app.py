from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello, Suresh! DevSecOps Demo is Working 🎉"

if __name__ == '__main__':
    app.run(debug=True)
