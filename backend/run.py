from flask import Flask, request # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome home!!"

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return "Hello from Post"
    return "Hello from /hello"

if __name__ == '__main__':
    app.run(debug=True)