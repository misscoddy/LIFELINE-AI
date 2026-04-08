import json
import random
import time
from fastapi import FastAPI
from fastapi.responses import JSONResponse

def log_start(task_id: str):
    print(f"(START) {task_id}")

def log_step(step_description: str):
    print(f"(STEP) {step_description}")

def log_end(result_description: str):
    print(f"(END) {result_description}")

def simulate_evacuation(prompt: str):
    log_start("Evacuation Simulation")
    log_step("Analyzing the prompt")
    time.sleep(0.1)
    log_step("Planning evacuation routes")
    time.sleep(0.1)
    log_step("Simulating people movement")
    people_moved = random.randint(8,10)
    log_step(f"{people_moved} people reached exits safely")
    output = {"prompt": prompt, "people_evacuated": people_moved, "status": "Simulation complete"}
    log_end(json.dumps(output))
    return output

app = FastAPI()

@app.post("/reset")
def openenv_reset():
    return JSONResponse({"status":"ok"})

@app.get("/validate")
def openenv_validate():
    return JSONResponse({"status":"ok"})

@app.post("/inference")
def openenv_inference(payload: dict):
    prompt = payload.get("prompt", "Default prompt")
    return JSONResponse(simulate_evacuation(prompt))
