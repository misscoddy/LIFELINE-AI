# inference.py
import json
import random
import time
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# -------------------------
# Dummy environment for Phase 1
# -------------------------
class DummyEnv:
    def reset(self, task_id="1"):
        # Return a dummy observation (just enough for OpenEnv to accept)
        return {"task_id": task_id, "people_evacuated": 0}

    def step(self, action):
        # Return dummy step result
        return {"status": "ok"}, {"value": random.randint(0, 10)}, False, {}

env = DummyEnv()

# -------------------------
# Pydantic models
# -------------------------
class ResetRequest(BaseModel):
    task_id: Optional[str] = None

class InferenceRequest(BaseModel):
    prompt: Optional[str] = None

# -------------------------
# FastAPI app
# -------------------------
app = FastAPI()

@app.post("/reset")
def reset(request: Optional[ResetRequest] = None):
    """Start a new episode safely (works with or without body)."""
    try:
        task_id = str(request.task_id) if request and request.task_id else "1"
        obs = env.reset(task_id=task_id)
        return obs  # Phase 1 only cares that this returns JSON
    except Exception as e:
        return {"error": str(e)}

@app.get("/validate")
def validate():
    return {"status": "ok"}

@app.post("/inference")
def inference(payload: Optional[InferenceRequest] = None):
    prompt = payload.prompt if payload and payload.prompt else "default prompt"
    # Dummy simulation
    people_evacuated = random.randint(8, 10)
    result = {
        "prompt": prompt,
        "people_evacuated": people_evacuated,
        "status": "done"
    }
    return result

# -------------------------
# Phase 1 quick test mode
# -------------------------
if __name__ == "__main__":
    print("Running Phase 1 test locally")
    print("Reset:", reset())
    print("Validate:", validate())
    print("Inference:", inference(InferenceRequest(prompt="Test")))
