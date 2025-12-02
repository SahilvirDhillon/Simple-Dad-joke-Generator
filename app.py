import requests
from flask import Flask, jsonify, redirect

app = Flask(__name__)

API_URL = "https://icanhazdadjoke.com/"


def get_dad_joke():
    headers = {
        "Accept": "application/json",
        "User-Agent": "NET2008-DadJokeGenerator (your-email@example.com)"
    }

    response = requests.get(API_URL, headers=headers, timeout=5)
    response.raise_for_status()
    data = response.json()
    return data.get("joke", "No joke found.")


@app.route("/")
def home():
    # Automatically redirect to /joke
    return redirect("/joke")


@app.route("/joke")
def joke():
    try:
        joke_text = get_dad_joke()
        return jsonify({"joke": joke_text})
    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch a dad joke.", "details": str(e)}), 502


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
