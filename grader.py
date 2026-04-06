def run_grader(env, agent_fn):
    obs = env.reset()
    total = 0

    for _ in range(50):
        action = agent_fn(obs)
        obs, reward, done, _ = env.step(action)
        total += reward.value
        if done:
            break

    if total > 100:
        return 1.0
    elif total > 0:
        return 0.5
    else:
        return 0.0