import json
import boto3

MODEL_ID = "us.anthropic.claude-haiku-4-5-20251001-v1:0"

SYSTEM_PROMPT = """
You are a federal health intake triage assistant.

Use only the provided text.
Do not use real protected health information.
Return only valid JSON with these fields:

category
urgency
missing_fields
recommended_next_action
risk_flags
plain_language_summary
"""

INPUT_TEXT = """
A community clinic is submitting a quarterly report for a federal grant.
They included total patients served and budget spend, but did not include
accessibility accommodations or supporting evidence for outreach activities.
"""

client = boto3.client("bedrock-runtime", region_name="us-east-1")

response = client.converse(
    modelId=MODEL_ID,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "text": f"{SYSTEM_PROMPT}\n\nInput:\n{INPUT_TEXT}"
                }
            ],
        }
    ],
    inferenceConfig={
        "maxTokens": 500,
        "temperature": 0.1,
    },
)

output = response["output"]["message"]["content"][0]["text"]


def clean_json_output(text: str) -> str:
    text = text.strip()

    if text.startswith("```json"):
        text = text.removeprefix("```json").strip()

    if text.startswith("```"):
        text = text.removeprefix("```").strip()

    if text.endswith("```"):
        text = text.removesuffix("```").strip()

    return text


cleaned_output = clean_json_output(output)

try:
    print(json.dumps(json.loads(cleaned_output), indent=2))
except json.JSONDecodeError:
    print("Model returned non-JSON output:")
    print(output)