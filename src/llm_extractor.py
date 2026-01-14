from groq import Groq
import json
import os

# Initialize Groq client
client = Groq(
    api_key=os.getenv("Groq API KEY")
)

SYSTEM_PROMPT = """
You are an AI system trained to extract metadata from legal agreements.

Guidelines:
- Values may appear in different wording or formats
- Infer agreement value, dates, and party names if clearly mentioned
- Party names usually appear in the introductory clauses
- If a field is truly not present, return null
- Return STRICTLY valid JSON
"""

USER_PROMPT_TEMPLATE = """
Extract the following fields from the document text:

- Agreement Value
- Agreement Start Date
- Agreement End Date
- Renewal Notice (Days)
- Party One
- Party Two

Return output in JSON with exactly these keys:
Agreement Value
Agreement Start Date
Agreement End Date
Renewal Notice (Days)
Party One
Party Two

Document Text:
----------------
{document_text}
"""

import re
import json

def extract_metadata(document_text: str) -> dict:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": USER_PROMPT_TEMPLATE.format(
                    document_text=document_text
                )
            }
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    print("\n===== RAW LLM OUTPUT =====\n")
    print(content)
    print("\n==========================\n")

    # ✅ Extract ONLY the JSON block using regex
    match = re.search(r"\{[\s\S]*\}", content)
    if not match:
        raise ValueError("No JSON object found in LLM response")

    json_str = match.group(0)

    return json.loads(json_str)
