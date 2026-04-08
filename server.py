from env import FarmerSchemeEnv

def main():
    env = FarmerSchemeEnv()

    obs = env.reset()
    print("START")

    total_reward = 0

    for step in range(3):
        query = obs["query"].lower()

        if "damage" in query or "rain" in query:
            action = {
                "scheme": "Crop Insurance",
                "explanation": "Farmers get help if crop is damaged"
            }
        elif "money" in query or "loan" in query:
            action = {
                "scheme": "Kisan Credit Card",
                "explanation": "Farmers get easy loan"
            }
        else:
            action = {
                "scheme": "PM Kisan",
                "explanation": "Farmers get yearly support"
            }

        obs, reward, done, _ = env.step(action)
        total_reward += reward

        print(f"STEP {step+1}: reward={reward}")

    print("END")
    print("Final Score:", total_reward)
