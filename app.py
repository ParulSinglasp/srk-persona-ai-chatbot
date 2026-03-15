from flask import Flask, request, jsonify, render_template
import json
from openai import OpenAI
import os
app = Flask(__name__)

import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load persona examples
with open("persona_examples.json", "r") as f:
    examples = json.load(f)

system_prompt = """
You are Shah Rukh Khan, the famous Bollywood actor.

You speak in a charming, emotional, dramatic Bollywood style.

Your personality traits:
- witty
- motivational
- philosophical
- charismatic

You often use movie metaphors like:
life is like a film
the hero never gives up
the climax is yet to come

Speak warmly and inspire people.
Keep answers between 2-4 sentences.
"""

def build_messages(user_input):

    messages = [{"role": "system", "content": system_prompt}]

    for ex in examples:
        messages.append({"role": "user", "content": ex["user"]})
        messages.append({"role": "assistant", "content": ex["srk"]})

    messages.append({"role": "user", "content": user_input})

    return messages

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    messages = build_messages(user_message)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    reply = response.choices[0].message.content

    return jsonify({"reply": reply})

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)