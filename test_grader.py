from environment import EvacuationEnv
from grader import run_grader
from baseline_agent import simple_agent

for level in ["easy", "medium", "hard"]:
    env = EvacuationEnv(level)
    score = run_grader(env, simple_agent)
    print(level, score)