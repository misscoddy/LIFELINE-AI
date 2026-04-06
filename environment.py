import random
from models import Observation, Action, Reward   # ✅ NO env here

class EvacuationEnv:
    def __init__(self, level="easy"):
        self.level = level
        self.size = 7
        self.reset()

    def reset(self):
        self.agent = [0, 0]

        if self.level == "easy":
            self.civilians = [[6, 6]]
            self.hazards = [[3, 3]]

        elif self.level == "medium":
            self.civilians = [[6, 6], [5, 2]]
            self.hazards = [[3, 3], [4, 4]]

        else:
            self.civilians = [[6, 6], [5, 2], [2, 5]]
            self.hazards = [[3, 3], [4, 4], [1, 3]]

        return self.state()

    def state(self):
        return Observation(
            agent=self.agent,
            civilians=self.civilians,
            hazards=self.hazards
        )

    def move_hazards(self):
        for h in self.hazards:
            h[0] = max(0, min(self.size-1, h[0] + random.choice([-1,0,1])))
            h[1] = max(0, min(self.size-1, h[1] + random.choice([-1,0,1])))

    def step(self, action: Action):
        move = action.move

        if move == 0: self.agent[0] -= 1
        if move == 1: self.agent[0] += 1
        if move == 2: self.agent[1] -= 1
        if move == 3: self.agent[1] += 1

        self.agent[0] = max(0, min(self.agent[0], self.size-1))
        self.agent[1] = max(0, min(self.agent[1], self.size-1))

        self.move_hazards()

        reward = -1
        done = False

        if self.agent in self.civilians:
            self.civilians.remove(self.agent)
            reward += 50

        if self.agent in self.hazards:
            reward = -80
            done = True

        if len(self.civilians) == 0:
            reward += 150
            done = True

        return self.state(), Reward(value=reward), done, {}