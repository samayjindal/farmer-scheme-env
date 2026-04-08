import os
from env import FarmerSchemeEnv

API_BASE_URL = os.getenv("API_BASE_URL", "")
MODEL_NAME = os.getenv("MODEL_NAME", "")
HF_TOKEN = os.getenv("HF_TOKEN")

def run_agent():
    print("START")

    env = FarmerSchemeEnv()
    total_reward = 0

    for step in range(3):
        obs = env.reset()
        query = obs["query"].lower()

        if "damage" in query or "rain" in query:
            scheme = "Crop Insurance"
            explanation = "Farmers get help if crop is damaged"
        elif "money" in query or "loan" in query:
            scheme = "Kisan Credit Card"
            explanation = "Farmers get easy loan"
        else:
            scheme = "PM Kisan"
            explanation = "Farmers get yearly support"

        action = {
            "scheme": scheme,
            "explanation": explanation
        }

        obs, reward, done, _ = env.step(action)
        total_reward += reward

        print(f"STEP {step+1}: reward={reward}")

    print("END")
    print("Final Score:", total_reward)

if __name__ == "__main__":
    run_agent()
