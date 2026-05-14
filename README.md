# Health Intake Triage Assistant

Minimal Python proof of concept for using Amazon Bedrock to triage mock federal health intake text.

The script sends a sample clinic grant-reporting scenario to Bedrock and returns structured JSON with:

- category
- urgency
- missing fields
- recommended next action
- risk flags
- plain-language summary

## Model

Uses Anthropic Claude Haiku 4.5 through Amazon Bedrock:

```text
us.anthropic.claude-haiku-4-5-20251001-v1:0
```

## Run

```bash
export AWS_PROFILE=health-triage
uv run python src/triage.py
```

## Notes

This repo uses mock data only. Do not submit real protected health information or sensitive agency data.
