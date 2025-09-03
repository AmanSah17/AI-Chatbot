from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=  os.environ.get("GROQ_API_KEY"),)



class chatRequest(BaseModel):
    message : str 




app = FastAPI()



# Since our frintend runs on react.js / JavaScript language and backend frame , for this project we are using FastAPI - python framework.
# This we need to establish connection between the cross - oringin request services from the above modules.

app.add_middleware(CORSMiddleware,
                   allow_origins = ["*"],
                   allow_methods = ["*"],
                   allow_headers = ["*"],
                   allow_credentials = True)




'''
def get_bot_reponse(user_message):
    message = user_message.lower()
    if "hello" in message or "hi" in message:
        return "Helllo! How can i help you today!"
    else:
        return "Sorry, I don't understand that yet !"
    

'''







def get_bot_response(user_message):
    message=user_message.lower()

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="llama-3.3-70b-versatile",
        stream=False,
    )

    return chat_completion.choices[0].message.content


@app.post("/chat")
def chat(request: chatRequest):
    reply = get_bot_response(request.message)  # fixed function name
    return {"reply": reply}


