from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

# print("HELLO FROM API KEY",os.getenv("GOOGLE_API_KEY"))

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1)

while True:
    user=input("Enter your question: ")
    if str(user).lower() in ["exit","quit"]:
        print("Exiting the program.")
        exit()
    response = llm.invoke(user)
    print(response.content)
