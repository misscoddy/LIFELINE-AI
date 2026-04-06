import random
from models import Action   # ✅ correct import

def simple_agent(obs):
    return Action(move=random.randint(0, 3))