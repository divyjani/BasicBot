from pydantic import BaseModel,Field
from typing import Dict,Annotated
class Output(BaseModel):
    summary:str=Field(...,description="Summary of the conversation",max_length=400)
    metadata:str=Field(...,description="Metadata about the conversation",max_length=160)
    
class OP(BaseModel):
    answer:Annotated[str,Field(...,description="Answer in 5 lines")]
    metadata:Annotated[str,Field(...,description="The data about at which time and date this api is called ")]
    
