from ast import List
from unittest.mock import Base
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List



class Fruit(BaseModel):
  name: str
  
class Fruits(BaseModel):
  fruits: List[Fruit]

  
app = FastAPI()

origin = [
  "http://localhost:5173",
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origin,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

memory_db ={"fruits":[]}

#GET request method
@app.get("/fruits", response_model=Fruits)
async def get_fruits():
  return Fruits(fruits=memory_db["fruits"])

#POST request method
@app.post("/fruits", response_model=Fruit)
async def add_fruit(fruit: Fruit):
  memory_db["fruits"].append(fruit)
  return fruit

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)