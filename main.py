from email.policy import default
from operator import truediv
from pickle import FALSE
from fastapi import FastAPI, Body, Depends
import uvicorn
from app.model import PKMSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer


pkms =[
    {
        "id":1,
        "title": "bla bla bla",
        "Content" : "bla bla bla bla bla bla bla"
    },
    {
        "id":2,
        "title": "ble ble ble",
        "Content" : "ble ble ble ble ble ble ble"
    },
        {
        "id":3,
        "title": "bli bli bli",
        "Content" : "bli bli bli bli bli bli bli bli bli"
    }
]

users=[]

app = FastAPI()

# Get root
@app.get("/", tags=["Root"])
def home():
    return{"Data": "API PKM with JWT authentication"}

# Get PKMs
@app.get("/get_all_pkms", tags=["Pokemon"])
def get_all_pkms():
    return {"data":pkms}

#Get PKMs by id
@app.get("/get_pkm_byid", tags=["Pokemon"])
def get_pkm_byid(id:int):
    if id > len(pkms):
        return{
            "error":"ID doens't exist in the databse."
        }
    for post in pkms:
        if post["id"] == id:
            return {"data":post}


# Add PKM
@app.post("/add_pkm", dependencies=[Depends(jwtBearer())], tags=["Pokemon"])
def add_pkm(pkm:PKMSchema):
    pkm.id=len(pkms)+1
    pkms.append(pkm.dict())
    return{
        "info":"Post Added!"
    }

# Add USR
@app.post("/user/signup", tags=["User"])
def add_user(usr:UserSchema = Body(default=None)):
   users.append(usr)
   return signJWT(usr.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False
    
@app.post("/user/login", tags=["User"])
def user_login(usr: UserLoginSchema = Body(default=None)):
    if check_user(usr):
        return signJWT(usr.email)
    else:
        return {
            "error":"Invalid login details"
        }

    