from fastapi import FastAPI, WebSocket
from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from heyoo import WhatsApp

messenger = WhatsApp('375606318963977',  phone_number_id='15556278887')

#----------------------------

class LLM:
    def __init__(self):
        self.system_prompt = "Eres un asistente personal altamente capacitado para cualquier tipo de oficina y te llamas Sergio"
        self.model_Ollama = "qwen2:7b-instruct"
        self.llm = Ollama(model=self.model_Ollama,
                          callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
                          temperature=0.1,
                          system=self.system_prompt,
                          )
    
    def getLLM(self):
        return self.llm

user = LLM()

#----------------------------
#uvicorn main:app --reload

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/nombre/")
async def hiName(name: str):
    return {"message": f"Hello {name}"}

@app.get('/obtenerPrompt/{prompt}')
async def prompt(prompt: str):
    llm = user.getLLM()
    messsage = [
            HumanMessage(content=prompt)
        ]
    return llm.invoke(messsage)