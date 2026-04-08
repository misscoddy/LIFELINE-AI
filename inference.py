import os
import json
import random
import time
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

# -------------------------------
# Environment Variables
# -------------------------------
API_BASE_URL     = os.getenv("API_BASE_URL", "http://localhost:8000")
MODEL_NAME       = os.getenv("MODEL_NAME", "evacuation_model")
HF_TOKEN         = os.getenv("HF_TOKEN")           # optional
LOCAL_IMAGE_NAME = os.getenv("LOCAL_IMAGE_NAME")  # optional

# -------------------------------
# Logging helpers
# -------------------------------
def log_start(task_id: str):
    print(f"(START) {task_id}")

def log_step(step_description: str):
    print(f"(STEP) {step_description}")

def log_end(result_description: str):
    print(f"(END) {result_description}")

# -------------------------------
# Dummy inference function
# -------------------------------
def simulate_evacuation(prompt: str, task_id: str = "Evacuation Simulation"):
    log_start(task_id)
    log_step("Analyzing the prompt")
    time.sleep(0.5)
    log_step("Planning evacuation routes")
    time.sleep(0.5)
    log_step("Simulating people movement")
    people_moved = random.randint(8, 10)
    log_step(f"{people_moved} people reached exits safely")
    output = {"prompt": prompt, "people_evacuated": people_moved, "status": "Simulation complete"}
    log_end(json.dumps(output))
    return output

# -------------------------------
# FastAPI server for OpenEnv
# -------------------------------
app = FastAPI()

@app.post("/reset")
def openenv_reset():
    return JSONResponse({"status": "ok"})

@app.get("/validate")
def openenv_validate():
    return JSONResponse({"status": "ok"})

@app.post("/inference")
def openenv_inference(payload: dict):
    prompt = payload.get("prompt", "Default prompt")
    result = simulate_evacuation(prompt)
    return JSONResponse(result)

# -------------------------------
# Run server if executed directly
# -------------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
