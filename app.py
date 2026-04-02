from flask import Flask,request, jsonify,render_template
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = Groq(api_key = os.getenv("GROQ_API_KEY"))
messages = [
    {"role" :"system" , "content" : "you are a helpful assistant named Zeus"}
]

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/chat", methods = ["POST"])

def chat():
    data = request.json
    user_message = data["message"]
    messages.append({"role" : "user" , "content" : user_message})
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = messages
    )
    reply = response.choices[0].message.content
    messages.append({"role" : "assistant" , "content" : reply})
    return jsonify({"reply" : reply})

app.run(debug = True)
