from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

subjects = [
    "A legendary Bollywood Superstar",
    "Your crush's overprotective brother",
    "A very judgmental HR Manager",
    "The person who left the sink dirty",
    "A 'Life Coach' with zero followers",
    "An Instagram influencer without a filter",
    "The guy who keeps 'replying all' to emails",
    "A politician caught eating street food",
    "A suspiciously wealthy 'Crypto King'",
    "The ghost of an angry Math teacher"
]

actions = [
    "gets caught sniffing a stranger's hair",
    "accidentally sends a 'Love You' text to the CEO",
    "forgets their pants during a TED Talk",
    "tries to flirt with a Chatbot",
    "breaks into a dance in a silent library",
    "gets stuck in a baby swing for 6 hours",
    "cries while reading a menu at a fancy restaurant",
    "challenges a toddler to a wrestling match",
    "gets banned from a local 'All You Can Eat' buffet",
    "mistakes a trash can for a VIP seat"
]

places = [
    "at a high-speed blind date",
    "inside a very small elevator with their ex",
    "during a live televised yoga session",
    "in the middle of a serious court hearing",
    "at a wedding for two goldfish",
    "on a first date at a public toilet",
    "while hiding under a table in the office",
    "at a 'No Screaming' meditation retreat",
    "inside a haunted Vada Pav stall",
    "on a treadmill at 3:00 AM"
]

def generate_news():
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    return f"🚨 BREAKING NEWS: {subject} {action} {place}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate")
def generate():
    headline = generate_news()
    return jsonify({"headline": headline})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
