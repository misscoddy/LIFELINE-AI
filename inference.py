# inference.py
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# -------------------------
# Minimal Env for Phase 1
# -------------------------
class DummyEnv:
    def reset(self, task_id="1"):
        return {"task_id": task_id, "people_evacuated": 0}

    def step(self, action):
        return {"status": "ok"}, {"value": 0}, False, {}

env = DummyEnv()

# -------------------------
# Request Models
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
def reset(request: ResetRequest):
    """Phase 1 safe reset"""
    try:
        task_id = str(request.task_id) if request.task_id else "1"
        obs = env.reset(task_id=task_id)
        return obs
    except Exception as e:
        return {"error": str(e)}

@app.get("/validate")
def validate():
    return {"status": "ok"}

@app.post("/inference")
def inference(payload: InferenceRequest):
    prompt = payload.prompt if payload.prompt else "default"
    return {"prompt": prompt, "people_evacuated": 0, "status": "done"}
