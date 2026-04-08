# inference.py
import os
import json
import random
import time

# -------------------------------
# Environment Variables (optional)
# -------------------------------
API_BASE_URL     = os.getenv("API_BASE_URL", "http://localhost:8000")
MODEL_NAME       = os.getenv("MODEL_NAME", "evacuation_model")
HF_TOKEN         = os.getenv("HF_TOKEN")           # optional, not used here
LOCAL_IMAGE_NAME = os.getenv("LOCAL_IMAGE_NAME")  # optional, not used here

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
# Dummy inference functions
# -------------------------------
def simulate_evacuation(prompt: str, task_id: str = "Evacuation Simulation"):
    """Simulates evacuation steps with structured logging."""
    log_start(task_id)
    
    log_step("Analyzing the prompt")
    time.sleep(0.5)  # simulate processing
    
    log_step("Planning evacuation routes")
    time.sleep(0.5)
    
    log_step("Simulating people movement")
    people_moved = random.randint(8, 10)
    log_step(f"{people_moved} people reached exits safely")
    
    output = {
        "prompt": prompt,
        "people_evacuated": people_moved,
        "status": "Simulation complete"
    }
    log_end(json.dumps(output))
    return output

def generate_dummy_response(prompt: str, task_id: str = "Dummy Response"):
    """Dummy LLM-style response without OpenAI."""
    log_start(task_id)
    log_step("Processing prompt internally")
    time.sleep(0.3)
    
    choices = ["Option A", "Option B", "Option C"]
    selected = random.choice(choices)
    log_step(f"Selected {selected} as response")
    
    result = {
        "prompt": prompt,
        "response": selected
    }
    log_end(json.dumps(result))
    return result

def multi_step_simulation(prompt: str, task_id: str = "Multi-step Simulation"):
    """Runs several dummy steps for complex simulation."""
    log_start(task_id)
    steps = ["Initialize environment", "Spawn agents", "Move agents", "Check collisions", "Finalize results"]
    
    results = {}
    for step in steps:
        log_step(step)
        time.sleep(0.3)
        results[step] = f"{random.randint(1,10)} agents processed"
    
    log_end(json.dumps(results))
    return results

# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    prompt1 = "Simulate an evacuation scenario with 10 people and 2 exits."
    simulate_evacuation(prompt1)
    
    prompt2 = "Choose best exit strategy"
    generate_dummy_response(prompt2)
    
    prompt3 = "Run full multi-step agent simulation"
    multi_step_simulation(prompt3)