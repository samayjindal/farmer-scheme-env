import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Action(BaseModel):
    scheme: str
    explanation: str

tasks = [
    {"query": "I need money help", "answer": "Kisan Credit Card"},
    {"query": "My crop got damaged due to rain", "answer": "Crop Insurance"},
    {"query": "I have small land and need financial support", "answer": "PM Kisan"}
]

current_task = {}

@app.post("/reset")
def reset():
    global current_task
    current_task = random.choice(tasks)
    return {"query": current_task["query"]}

@app.post("/step")
def step(action: Action):
    correct = current_task["answer"]
    reward = 0

    if action.scheme.lower() == correct.lower():
        reward += 1
    else:
        reward -= 1

    if len(action.explanation.split()) <= 12:
        reward += 0.5

    if "farmer" in action.explanation.lower():
        reward += 0.2

    return {
        "observation": {"query": current_task["query"]},
        "reward": reward,
        "done": True,
        "info": {}
    }

@app.get("/state")
def state():
    return current_task
