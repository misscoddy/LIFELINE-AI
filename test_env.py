from environment import EvacuationEnv
from models import Action
import random

env = EvacuationEnv("easy")
obs = env.reset()

for i in range(5):
    action = Action(move=random.randint(0,3))
    obs, reward, done, _ = env.step(action)
    print("Step:", i+1, "Reward:", reward.value, "Done:", done)