import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import HumanMessage, SystemMessage

#from src.config import instruction

load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

def ask_bot(user_message):
    
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    
    
    respones=llm.invoke(user_message)
    return respones.content

if __name__=="__main__":
    print("Welcome to chatbot")
    print(GOOGLE_API_KEY)
    user_message = "What is transformer?"
    response=ask_bot(user_message)
    print(response)