from langchain_groq import ChatGroq
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from prompts.prompt import TEACHER
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage
# from langchain_core.chains import ConversationChain
# from langchain_core.memory import ConversationBufferMemory
# from langchain.chains import ConversationChain
# from langchain.memory import ConversationBufferMemory
from models.output import OP
from langchain_core.output_parsers import PydanticOutputParser
import os

load_dotenv()

model= ChatGroq(
    model="llama-3.1-8b-instant"
)
# st_model=model.with_structured_output(OP)

parser=PydanticOutputParser(pydantic_object=OP)
# model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1)
# api_key=os.getenv("API_KEY")

# template=PromptTemplate(
#     template=TEACHER,
#     input_variables=["history","std","board","input"],
#                     validate_template=True)
# prompt=template.invoke({"std":8,"board":"CBSE"})
chat_history=[]

template=ChatPromptTemplate.from_messages([("system",TEACHER+ "\n\nYou must respond only in valid JSON.\n{format_instructions}"),
MessagesPlaceholder(variable_name="chat_history"),
("human","{input}"),
])

prompt = template.partial(
    format_instructions=parser.get_format_instructions()
)
# memory=ConversationBufferMemory()
# chain=ConversationChain(llm=model,prompt=template,memory=memory)

# prompt=template.invoke({"std":8})
# print(prompt)


chain=prompt|model|parser

n=0
while True:
    if n>4:
        print("Exiting the program.")
        exit()
    
    user =str(input("Enter your question: "))
    
    if user.lower() in ["exit","quit"]:
        print("Exiting the program.")
        exit()            
    obj={"std":"8",
        "board":"CBSE",
        "chat_history":chat_history,
        "input":user
        }
    resp=chain.invoke(obj)
    
    # resp=chain.predict(input=user,std="8",board="CBSE")
    
    chat_history.append(HumanMessage(content=user)) 
    
    chat_history.append(AIMessage(content=resp.answer))
    
    # chat_history.append(SystemMessage(content=template.invoke(obj)),HumanMessage(content=resp.content))
    print(resp)
    
#     prompt_value = chain.prompt.format_prompt(
#     input=user,
#     std="8",
#     board="CBSE",
#     history=memory.buffer
# )

#     print(prompt_value.to_string())


    n+=1



