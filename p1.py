
from groq import Groq
import sys
from dotenv import load_dotenv
import os

load_dotenv()  

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
messages = [
    {"role" : "system" , "content" : "you are my personal assistant named Zeus."},
    {"role" : "user" , "content" : "My name is Taha."}
]
max_messages = 50
while True:
    question = input("You:\n ")
    sys.stdout.flush()
    if question.lower() == "quit":
        print("Zeus : Goodbye...")
        break
    messages.append({"role": "user", "content": question })
    try:
        response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages = messages
        )
    except Exception as e:
        print("Error.",e)
        continue
    reply = response.choices[0].message.content
    print("Zeus..\n", reply, "\n")
    messages.append({"role" : "assistant" , "content" : reply})
    if len(messages) > max_messages:
        messages = messages[-max_messages:]




