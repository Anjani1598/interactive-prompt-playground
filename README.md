

# Interactive Prompt Playground

This is an interactive Python playground to explore how OpenAI’s language models (GPT-3.5, GPT-4, GPT-4o) respond to different parameter settings when generating product descriptions. It allows you to customize input prompts, select the model, and control generation parameters such as temperature, max tokens, frequency penalty, and presence penalty.

## 🚀 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/interactive-prompt-playground.git
   cd interactive-prompt-playground
   ```

2. **Set up environment variables:**
   Create a `.env` file and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_key
   ```

3. **Install dependencies:**

   ```bash
   pip install openai python-dotenv pandas
   ```

4. **Run the playground:**

   ```bash
   python playground.py
   ```

## ✨ Features

* ✅ **User Prompt Input:** Describe any product (e.g., "iPhone", "Tesla", "running shoes").
* ✅ **System Prompt Input:** Define the tone or role of the assistant (default: product description writer).
* ✅ **Parameter Controls:**

  * **Temperature** (e.g., 0.0, 0.7, 1.2)
  * **Max Tokens** (e.g., 50, 150, 300)
  * **Frequency Penalty** (e.g., 0.0, 1.5)
  * **Presence Penalty** (e.g., 0.0, 1.5)
* ✅ **Model Selection:** Choose between `gpt-3.5-turbo`, `gpt-4`, and `gpt-4o`.
* ✅ **Output Display:** See results of your selected configuration immediately.
* ✅ **Safe API Usage:** Environment variables keep your API key secure.

## 📊 Sample Output Table

| Model         | Temperature | Max Tokens | Freq Penalty | Pres Penalty | Output (excerpt)                              |
| ------------- | ----------- | ---------- | ------------ | ------------ | --------------------------------------------- |
| gpt-3.5-turbo | 0.0         | 50         | 0.0          | 0.0          | "The iPhone is a sleek, modern smartphone…"   |
| gpt-4o        | 1.2         | 300        | 1.5          | 0.0          | "Unleash your digital lifestyle with iPhone…" |

(*Note: actual content may vary, table excerpted for brevity*)

## ✍️ Reflection

Experimenting with temperature revealed significant variation in tone and creativity. At `temperature=0.0`, the model produced consistent, fact-based descriptions with minimal flair. Increasing the temperature to `0.7` introduced slightly more engaging phrases, while `1.2` led to vivid, sometimes poetic, language—highlighting how randomness affects expressiveness.

Adjusting frequency and presence penalties altered content diversity. With higher penalties, repetition was reduced and the model introduced more varied vocabulary. However, overly penalizing frequency sometimes led to verbose or tangential outputs. Each parameter combination shifts the balance between creativity, coherence, and verbosity, allowing fine-grained control of the assistant’s style.

---

Let me know if you'd like a downloadable `.md` version or a sample CSV/table generator for the results.
