import os
from openai import OpenAI

# Load API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Allow switching models via environment variable, default to gpt-3.5-turbo
MODEL = os.getenv("GENAI_MODEL", "gpt-3.5-turbo")

def interpret_prediction(result: dict) -> str:
    """
    Generate a natural language explanation for a prediction
    using an OpenAI model. Falls back if quota is exceeded.
    """
    msg = (
        f"System prediction = {result['prediction']} "
        f"(confidence {round(result['confidence']*100, 2)}%). "
        f"Explain this prediction and suggest next steps."
    )

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": msg}],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[GenAI Explanation Unavailable] {str(e)}"

if __name__ == "__main__":
    print(interpret_prediction({"prediction": 1, "confidence": 0.87}))
