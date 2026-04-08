from fastapi import FastAPI
from fastapi.responses import JSONResponse
from environment import EvacuationEnv
from models import Action

app = FastAPI()
env = None  # Global environment

# --- Reset environment ---
@app.post("/reset")
def reset(level: str = "easy"):
    global env
    env = EvacuationEnv(level)
    obs = env.reset()
    return JSONResponse({"state": obs.dict()})

# --- Step endpoint ---
@app.post("/step")
def step(action: dict):
    global env
    if env is None:
        return JSONResponse({"error": "Environment not initialized"}, status_code=400)

    act = Action(**action)
    obs, reward, done, _ = env.step(act)
    return JSONResponse({
        "state": obs.dict(),
        "reward": reward.value,
        "done": done
    })

# --- Validate endpoint ---
@app.get("/validate")
def validate():
    return JSONResponse({"status": "ok"})

# --- Local Phase 1 test ---
if __name__ == "__main__":
    env = EvacuationEnv("easy")
    obs = env.reset()
    print("Phase 1 local test OK")
