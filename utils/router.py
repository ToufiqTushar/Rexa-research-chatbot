import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()


api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY is not configured."
    )


client = Groq(
    api_key=api_key
)


def classify_question(question):
    """
    Classify a user question as either:
    - DOCUMENT
    - GENERAL
    """

    prompt = f"""
You are a question classifier for a research chatbot.

The chatbot may have a document uploaded by the user.

Classify the user's question into exactly ONE category:

DOCUMENT
GENERAL

DOCUMENT:
Use this category when the user is asking about information
that would reasonably be expected to come from an uploaded
document.

GENERAL:
Use this category for general knowledge, casual questions,
programming questions, explanations, or anything that does
not specifically require the uploaded document.

USER QUESTION:
{question}

Return ONLY one word:

DOCUMENT

or

GENERAL
"""


    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",

        messages=[
            {
                "role": "system",
                "content": (
                    "You are a strict question classifier. "
                    "Return only DOCUMENT or GENERAL."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0,
        max_completion_tokens=10,
        top_p=1
    )


    result = (
        completion
        .choices[0]
        .message
        .content
        .strip()
        .upper()
    )


    if "DOCUMENT" in result:
        return "DOCUMENT"

    return "GENERAL"