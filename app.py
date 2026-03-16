# adding additional modules for connecting HTML TO FASTAPI:
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import FastAPI
from groq import Groq


app = FastAPI()
templates = Jinja2Templates(directory="templates")

client = Groq(api_key="API_KEY")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/chat")
def chat(query: str):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": query}
        ]
    )

    answer = response.choices[0].message.content

    return {"response": answer}