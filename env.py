import random

class FarmerSchemeEnv:
    def __init__(self):
        self.tasks = [
            {"query": "I need money help", "answer": "Kisan Credit Card"},
            {"query": "My crop got damaged due to rain", "answer": "Crop Insurance"},
            {"query": "I have small land and need financial support", "answer": "PM Kisan"}
        ]
        self.current_task = None

    def reset(self):
        self.current_task = random.choice(self.tasks)
        return {"query": self.current_task["query"]}

    def step(self, action):
        correct = self.current_task["answer"]
        reward = 0

        if action.get("scheme", "").lower() == correct.lower():
            reward += 1
        else:
            reward -= 1

        explanation = action.get("explanation", "")

        if len(explanation.split()) <= 12:
            reward += 0.5

        if "farmer" in explanation.lower():
            reward += 0.2

        done = True

        return (
            {"query": self.current_task["query"]},
            reward,
            done,
            {}
        )

    def state(self):
        return {
            "query": self.current_task["query"] if self.current_task else ""
        }
