from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

subjects = [
    "Salman Khan",
    "Aamir Khan",
    "Akshay Kumar",
    "Hrithik Roshan",
    "A disgruntled Halwai",
    "Your Ex-Boss",
    "An over-enthusiastic Neighborhood Aunty",
    "Narendra Modi's personal stylist",
    "A ChatGPT-obsessed Junior Developer",
    "The guy who sells Vada Pav outside the stadium",
    "A very confused Mumbai local train commuter",
    "A gym bro who forgot his protein shake",
    "An AI that thinks it is a Punjabi singer",
    "A billionaire trying to use a coupon"
]

actions = [
    "launches",
    "cancels",
    "announces",
    "reveals",
    "apologizes",
    "marries",
    "starts a protest against gravity",
    "performs an aggressive belly dance",
    "accidentally eats a whole laptop",
    "challenges a stray dog to a rap battle",
    "tries to pay for a Ferrari with Monopoly money",
    "invests all savings in a 'Magic Churan' business",
    "files a police complaint against a mosquito",
    "tries to install Windows on a toaster",
    "offers free spiritual advice"
]

places = [
    "at Red Fort",
    "in Mumbai local train",
    "in a meeting with PM",
    "during IPL match",
    "inside a crowded Metro during rush hour",
    "while stuck in a 4-hour Bangalore traffic jam",
    "at a grand funeral for a dead housefly",
    "on a Zoom call with the CEO (while shirtless)",
    "inside a giant pressure cooker",
    "on the moon, desperately looking for a 5G signal",
    "at the bottom of a cold bowl of Maggi",
    "on top of the Taj Mahal for a TikTok",
    "inside the pocket of a Bollywood star",
    "at a high-stakes Poker game in a Dhaba",
    "underneath a sleeping cow"
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
