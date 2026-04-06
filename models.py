from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    agent: List[int]
    civilians: List[List[int]]
    hazards: List[List[int]]

class Action(BaseModel):
    move: int  # 0 up, 1 down, 2 left, 3 right

class Reward(BaseModel):
    value: float