from fastapi import FastAPI, Query
from app.parser import str_parser, json_parser, pydantic_parser   # ✅ absolute import
app = FastAPI(title="Parser API")
@app.get("/parse/str")
def parse_str(data: str = Query(...)):
    return str_parser(data)

@app.get("/parse/json")
def parse_json(data: str = Query(...)):
    return json_parser(data)

@app.get("/parse/pydantic")
def parse_pydantic(data: str = Query(...)):
    return pydantic_parser(data)
