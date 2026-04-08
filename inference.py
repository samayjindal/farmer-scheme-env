import os
from env import FarmerSchemeEnv

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")

def run_agent():
    env = FarmerSchemeEnv()
    total_reward = 0

    for _ in range(3):
        obs = env.reset()
        query = obs["query"].lower()

        # Smart rule-based agent
        if "damage" in query or "rain" in query:
            scheme = "Crop Insurance"
            explanation = "Farmers get help if crop is damaged"
        elif "money" in query or "loan" in query:
            scheme = "Kisan Credit Card"
            explanation = "Farmers get easy loan at low interest"
        else:
            scheme = "PM Kisan"
            explanation = "Farmers get yearly financial support"

        action = {
            "scheme": scheme,
            "explanation": explanation
        }

        _, reward, _, _ = env.step(action)
        total_reward += reward

    print("Final Score:", total_reward)


if __name__ == "__main__":
    run_agent()