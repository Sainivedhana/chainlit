import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import HumanMessage, SystemMessage

#from src.config import instruction

load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def ask_bot(user_message):
    
    llm = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
    
    
    respones=llm.invoke(user_message)
    return respones.content

if __name__=="__main__":
    print("Welcome to chatbot")
    user_message = "What is transformer?"
    response=ask_bot(user_message)
    print(response)