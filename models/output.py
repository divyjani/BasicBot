from pydantic import BaseModel,Field

class Output(BaseModel):
    summary:Field(...,description="Summary of the conversation",max_length=400)
    metadata:Field(...,description="Metadata about the conversation",max_length=160)