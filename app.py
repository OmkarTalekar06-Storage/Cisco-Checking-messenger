from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    name = request.form['name']
    message = request.form['message']
    messages.append(f"{name}: {message}")
    return 'OK'

@app.route('/get')
def get():
    return jsonify(messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)