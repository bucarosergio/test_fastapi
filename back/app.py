#from langchain_core.messages import SystemMessage
#from langchain_core.prompts import MessagesPlaceholder
from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.document_loaders import PDFPlumberLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import PromptTemplate


class LLM:
    def __init__(self):
        self.system_prompt = "Eres un asistente personal altamente capacitado para cualquier tipo de oficina y te llamas Lourdes de León"
        self.model_Ollama = "qwen2:7b-instruct"
        self.llm = Ollama(model=self.model_Ollama,
                          callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
                          temperature=0.1,
                          system=self.system_prompt,
                          )
        
    def print_ans(self,prompt):
        self.promt = prompt
        messsage = [
            HumanMessage(content=self.promt)
        ]
        self.llm.invoke(messsage)

user = LLM()

while True:
    prompt = input("\nMensaje: ")
    if prompt == "exit":
        exit()
    user.print_ans(prompt)