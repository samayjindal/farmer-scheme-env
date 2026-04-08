import random

class FarmerSchemeEnv:
    def __init__(self):
        self.tasks = [
            {
                "query": "I need money help",
                "answer": "Kisan Credit Card",
                "difficulty": "easy"
            },
            {
                "query": "My crop got damaged due to rain",
                "answer": "Crop Insurance",
                "difficulty": "medium"
            },
            {
                "query": "I have small land and need financial support",
                "answer": "PM Kisan",
                "difficulty": "hard"
            }
        ]
        self.current_task = None

    def reset(self):
        self.current_task = random.choice(self.tasks)
        return {"query": self.current_task["query"]}

    def step(self, action):
        reward = 0
        correct = self.current_task["answer"]

        # Correct scheme
        if action["scheme"].lower() == correct.lower():
            reward += 1
        else:
            reward -= 1

        # Explanation quality (short + simple)
        if len(action["explanation"].split()) <= 12:
            reward += 0.5

        # Bonus if explanation contains farmer-friendly words
        if "farmer" in action["explanation"].lower():
            reward += 0.2

        done = True

        return {"query": self.current_task["query"]}, reward, done, {}