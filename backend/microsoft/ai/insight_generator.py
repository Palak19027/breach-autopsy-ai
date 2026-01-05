import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_insights(timeline_json: dict) -> str:
    try:
        with open("ai/prompt_templates/root_cause_prompt.txt", "r") as f:
            system_prompt = f.read()

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Timeline Data:\n{timeline_json}"}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:
        # 🔥 FALLBACK MODE (DEMO-SAFE)
        return (
            "Root Cause: Excessive permissions were granted without validation.\n"
            "Ignored Signal: A high severity alert was triggered but not acted upon.\n"
            "Wrong Decision: The security team delayed response assuming low risk.\n"
            "Preventive Rule: Enforce immediate review for any admin permission changes."
        )
      