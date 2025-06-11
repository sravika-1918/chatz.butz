from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot_logic import get_bot_reply

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")
    reply = get_bot_reply(user_message)
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
