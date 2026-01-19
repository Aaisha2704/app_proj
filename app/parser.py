import json
from pydantic import BaseModel, ValidationError
def str_parser(data: str):
    return {"length": len(data), "upper": data.upper(), "lower": data.lower()}
def json_parser(data: str):
    try:
        return {"parsed": json.loads(data)}
    except Exception as e:
        return {"error": str(e)}
class UserModel(BaseModel):
    name: str
    age: int
    email: str
def pydantic_parser(data: str):
    try:
        parsed = json.loads(data)
        user = UserModel(**parsed)
        return {"validated": user.dict()}
    except (ValidationError, Exception) as e:
        return {"error": str(e)}
