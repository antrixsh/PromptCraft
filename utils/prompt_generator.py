#--- SHUBHAM MHASKE
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
from langchain.llms import OpenAI
def generate_prompt(user_input):
    prompt = f"User Input: {user_input}\n\n"
    prompt += "for above please generate List of Prompt suitable for GPT models from basic to advance"
    print(prompt)
    llm = OpenAI(temperature=0.9)
    if prompt:
        response=llm(prompt)

    print(response)
    return response

#------------SHUBHAM MHASKE


