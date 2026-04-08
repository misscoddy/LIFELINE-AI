import json
import random
import time
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# --- Logging helpers ---
def log_start(task_id):
    print(f"(START) {task_id}")

def log_step(step):
    print(f"(STEP) {step}")

def log_end(result):
    print(f"(END) {result}")

# --- Dummy evacuation simulation ---
def simulate_evacuation(prompt):
    log_start("Evacuation Simulation")
    log_step("Analyzing prompt")
    time.sleep(0.1)
    log_step("Planning routes")
    time.sleep(0.1)
    log_step("Simulating people movement")
    people_moved = random.randint(8, 10)
    log_step(f"{people_moved} people reached exits safely")
    result = {"prompt": prompt, "people_evacuated": people_moved, "status": "done"}
    log_end(json.dumps(result))
    return result

# --- FastAPI app ---
app = FastAPI()

@app.post("/reset")
def reset():
    return JSONResponse({"status": "ok"})

@app.get("/validate")
def validate():
    return JSONResponse({"status": "ok"})

@app.post("/inference")
def inference(payload: dict):
    prompt = payload.get("prompt", "Default prompt")
    return JSONResponse(simulate_evacuation(prompt))

# --- Phase 1 quick test mode ---
if __name__ == "__main__":
    print("Running OpenEnv Phase 1 test")
    result = simulate_evacuation("Test prompt")
    print(result)
