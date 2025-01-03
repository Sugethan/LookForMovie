from pydantic import BaseModel, EmailStr, model_validator
from typing import Any

class logins_model(BaseModel):
    email: EmailStr
    password: str
    
class user_model(BaseModel):
    id: str
    name: str
    logins: logins_model
    
    @model_validator(mode="before")
    def map_logins(cls, data: dict[str, Any]):
        
        if "email" in data and "password" in data:
            data["logins"] = {
                "email": data.pop("email"),
                "password": data.pop("password"),
            }
        
        if "_id" in data and isinstance(data["_id"], dict) and "$oid" in data["_id"]:
            data["id"] = data["_id"]["$oid"]
            data.pop("_id")
        return data