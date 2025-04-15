
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import openai
import os
from glpi import creer_ticket_glpi

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.post("/api/messages")
async def message_handler(req: Request):
    data = await req.json()
    user_message = data.get("text", "Bonjour")

    if any(word in user_message.lower() for word in ["ticket", "incident", "souci", "problème"]):
        creer_ticket_glpi(description=user_message, user_email="user@example.com")
        return JSONResponse(content={"type": "message", "text": "Votre demande a été transmise au support technique. Un ticket a été créé."})

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Tu es un assistant support informatique professionnel, réponds en français."},
            {"role": "user", "content": user_message}
        ]
    )

    bot_reply = completion.choices[0].message['content']
    return JSONResponse(content={"type": "message", "text": bot_reply})
