from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from ask_bot import ask_chat_bot

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/call_function', methods=['POST'])
def call_function():
    data = request.get_json()
    print(data)
    question = data.get("question", "")
    result = ask_chat_bot(question)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
