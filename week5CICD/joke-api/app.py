from flask import Flask, jsonify
import random

app = Flask(__name__)

jokes = [
    "Why don’t developers like nature? It has too many bugs.",
    "Why did the developer go broke? Because he used up all his cache.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "What is a programmer’s favorite hangout place? The Foo Bar."
]

@app.route("/joke")
def joke():
    return jsonify({"JOKE": random.choice(jokes)})

@app.route("/")
def greeting():
    return jsonify({"message": "Welcome to the Joke API!, got to /joke to get a joke!"})

@app.route("/jokes")
def jokes_list():
    return jsonify({"JOKE": jokes})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
