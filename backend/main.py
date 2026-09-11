from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.get("/")
def home():
    return {"message": "Cloud Tasks API is running!"}

@app.get("/tasks")
def get_tasks():
    return tasks