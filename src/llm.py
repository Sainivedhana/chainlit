import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import HumanMessage, SystemMessage

from src.config import instruction

load_dotenv()

def ask_bot(user_message,instruction):
    
    model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=os.environ["g_api"], convert_system_message_to_human=True)
    
    
    respones=model(
    [
        SystemMessage(content=instruction),
        HumanMessage(content=user_message),
    ]
)
    
    return respones.content

if __name__=="__main__":
    user_message = "hi how are you?"
    respones=ask_bot(user_message, instruction)
    print(respones)