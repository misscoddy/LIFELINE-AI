from environment import EvacuationEnv
from baseline_agent import simple_agent

env = EvacuationEnv("medium")
obs = env.reset()

for _ in range(10):
    action = simple_agent(obs)
    obs, reward, done, _ = env.step(action)
    print(reward.value)
    if done:
        break