from env import FarmerSchemeEnv

env = FarmerSchemeEnv()

obs = env.reset()
print("Query:", obs["query"])

action = {
    "scheme": "Kisan Credit Card",
    "explanation": "Farmers get easy loan"
}

_, reward, _, _ = env.step(action)
print("Reward:", reward)