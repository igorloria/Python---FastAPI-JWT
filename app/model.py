from email.policy import default
from pydantic import BaseModel, Field, EmailStr

class PKMSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)
    class Config:
        schema_extra = {
            "pkm_demo":{
                "title" : "Some title about bla bla bla",
                "content" : "Content about bla bla bla"
            }
        }

class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class Config:
        user_schema = {
            "user_demo":{
                "name" : "Name 1",
                "email" : "email@email.com",
                "password":"123"
            }
        }
        
class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class Config:
        user_schema = {
            "user_demo":{
                "email" : "email@email.com",
                "password":"123"
            }
        }