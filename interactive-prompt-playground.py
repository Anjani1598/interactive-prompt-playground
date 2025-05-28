import itertools

import openai
from openai import OpenAI
import pandas as pd
from dotenv import load_dotenv

import os
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
  api_key = api_key,
)

user_prompt  = input("Ask Any product Description : ")
model = "gpt-4o-mini"  # Specify the model you want to use


# Parameters to vary
temperatures = [0.0, 0.7, 1.2]
max_tokens_list = [50, 150, 300]
frequency_penalties = [0.0, 1.5]
presence_penalties = [0.0, 1.5]

results = []


combinations = list(itertools.product(temperatures, max_tokens_list, frequency_penalties, presence_penalties))

print(f"Running {len(combinations)} combinations...")


# System prompt with default
system_prompt = input("Give System prompt: ") or "You are a helpful assistant who writes product descriptions."

def get_input_with_validation(prompt, default, value_type, min_val=None, max_val=None):
    while True:
        user_input = input(f"{prompt} [default={default}]: ").strip()
        if not user_input:
            return default
        try:
            value = value_type(user_input)
            if min_val is not None and value < min_val:
                print(f"❌ Value must be ≥ {min_val}. Please try again.")
                continue
            if max_val is not None and value > max_val:
                print(f"❌ Value must be ≤ {max_val}. Please try again.")
                continue
            return value
        except ValueError:
            print(f"❌ Please enter a valid {value_type.__name__}.")


temp = get_input_with_validation("Temperature", default=0.0, value_type=float, min_val=0.0, max_val=2.0)
max_tokens = get_input_with_validation("Max Tokens", default=50, value_type=int, min_val=1, max_val=4096)
freq_penalty = get_input_with_validation("Frequency Penalty", default=0.0, value_type=float, min_val=0.0, max_val=2.0)
pres_penalty = get_input_with_validation("Presence Penalty", default=0.0, value_type=float, min_val=0.0, max_val=2.0)


models = ["gpt-3.5-turbo", "gpt-4", "gpt-4o-mini"]
print("Select a model:")
for i, m in enumerate(models, start=1):
    print(f"{i}. {m}")

choice = input("Enter choice [default=1]: ") or "1"
model = models[int(choice) - 1]



try:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=temp,
        max_tokens=max_tokens,
        frequency_penalty=freq_penalty,
        presence_penalty=pres_penalty,
    )

    output = response.choices[0].message.content.strip()
    print("Output:", output)
    print("=" * 10)

    results.append({
        "Model": model,
        "Temperature": temp,
        "Max Tokens": max_tokens,
        "Frequency Penalty": freq_penalty,
        "Presence Penalty": pres_penalty,
        "Output": output
    })

    print(results)

except Exception as e:
    results.append({
        "Model": model,
        "Temperature": temp,
        "Max Tokens": max_tokens,
        "Frequency Penalty": freq_penalty,
        "Presence Penalty": pres_penalty,
        "Output": f"Error: {str(e)}"
    })
    print(results)


















