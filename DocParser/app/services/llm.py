import json
import os
from app.config import GEMINI_API_KEY

try:
    from google import genai
    client = genai.Client(api_key=GEMINI_API_KEY)
except:
    client = None

def generate_tests(node_texts):
    if not client:
        return [
            {"name": "Test 1", "steps": ["Step 1", "Step 2"], "expected": "Result"},
            {"name": "Test 2", "steps": ["Step A", "Step B"], "expected": "Outcome"}
        ]

    combined = "\n\n".join(node_texts)
    prompt = f"Generate 3 QA test cases (name, steps as array, expected result) for:\n\n{combined}"

    try:
        interaction = client.interactions.create(
            model="gemini-3.5-flash",
            input=prompt,
            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "steps": {"type": "array", "items": {"type": "string"}},
                            "expected": {"type": "string"}
                        }
                    }
                }
            }
        )
        return json.loads(interaction.output_text)
    except:
        return [
            {"name": "Fallback Test", "steps": ["Check manual"], "expected": "Correct info"}
        ]
