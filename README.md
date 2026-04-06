🚑 Evacuation AI Environment

📌 Overview

This project simulates a real-world evacuation scenario where an AI agent must rescue civilians while avoiding dangerous hazards.

Built as part of a hackathon, this environment follows the OpenEnv standard and is designed for reinforcement learning experiments.

---

🧠 Problem Statement

In emergency situations (fires, disasters), intelligent systems can assist in evacuation planning.

This environment models:

- Navigation under risk
- Decision-making under uncertainty
- Reward-based learning

---

⚙️ Core Features

✅ OpenEnv Compatible (reset, step, state)
✅ 3 Difficulty Levels (Easy, Medium, Hard)
✅ Dynamic Hazard Movement
✅ Reward-Based Learning System
✅ Baseline AI Agent Included
✅ Deterministic Grader System
✅ Visualization using Pygame

---

🎯 Environment Design

🧩 State (Observation)

- Agent Position
- Civilian Locations
- Hazard Locations

🎮 Actions

Action| Meaning
0| Move Up
1| Move Down
2| Move Left
3| Move Right

---

🎁 Reward System

Event| Reward
Step| -1
Rescue Civilian| +50
All Rescued| +150
Hit Hazard| -80

---

🧪 Difficulty Levels

Level| Description
Easy| 1 civilian, 1 hazard
Medium| 2 civilians, 2 hazards
Hard| 3 civilians, 3 hazards

---

📁 Project Structure

evacuation-env/
│
├── environment.py
├── models.py
├── grader.py
├── baseline_agent.py
├── visualize.py
├── test_env.py
├── test_agent.py
├── test_grader.py
├── requirements.txt
├── Dockerfile

---

🚀 Installation

python -m pip install -r requirements.txt

---

▶️ Run Instructions

python test_env.py
python test_agent.py
python test_grader.py
python visualize.py

---

🎮 Controls (Visualization)

- Press 1 → Easy
- Press 2 → Medium
- Press 3 → Hard
- Use Arrow Keys to move agent

---

🧠 Baseline Agent

A simple rule-based agent that:

- Moves randomly (baseline behavior)

---

🧪 Grader System

- Score range: 0 to 1
- Based on total reward

Score| Meaning
1.0| Excellent
0.5| Partial
0.0| Poor

---

🐳 Docker Support

docker build -t evacuation-ai .
docker run evacuation-ai

---

✅ Hackathon Compliance Checklist

✔ Real-world problem
✔ Minimum 3 tasks (Easy/Medium/Hard)
✔ Reward shaping (not binary)
✔ Deterministic grader
✔ Baseline agent included
✔ Dockerized
✔ Clean README

---
##Demo screenshot
![image alt](https://github.com/misscoddy/LIFELINE-AI/blob/6dfd48db1ce90288427ee687d5baeb7a7a8c9869/start.png)
![image alt](
![image alt](

✨ Future Improvements

- Smarter AI (RL-based agent)
- Better visualization (animations)
- Multi-agent coordination

---

👩‍💻 Author

Developed for Hackathon Submission 🚀
