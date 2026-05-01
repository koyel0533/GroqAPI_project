from groq import Groq
import os
from dotenv import load_dotenv,find_dotenv

def load_key():
   status=load_dotenv(find_dotenv(), override=True)
   client = Groq(api_key=os.getenv('GROQ_API_KEY'))
   return client
