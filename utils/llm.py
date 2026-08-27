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


def ask_llm(
    question,
    context=None,
    chat_history=None
):
    """
    Generate an answer using GPT-OSS-120B.

    context:
        Retrieved document context.
        None for general questions.

    chat_history:
        Previous conversation messages.
    """

    messages = []


    # -----------------------------------------
    # System message
    # -----------------------------------------

    if context:

        system_prompt = """
You are Rexa, an AI research assistant.

Your name is Rexa.

You were developed by Taufiq Zahan Tushar.

The user has uploaded a document.

Answer the user's question using the provided
document context.

IDENTITY RULES:
1. Your name is Rexa.
2. If the user asks "Who are you?", introduce yourself
   as Rexa, an AI research assistant.
3. If the user asks "What is your name?", say that
   your name is Rexa.
4. If the user asks who developed you, say that you
   were developed by Taufiq Zahan Tushar.
5. Do not introduce yourself as ChatGPT.
6. Do not claim that your name is ChatGPT.
7. If the user asks about the underlying model, explain
   that Rexa uses the GPT-OSS-120B model through the
   Groq API.

DOCUMENT RULES:
1. Use the document context as the primary source.
2. Do not invent information that contradicts the document.
3. If the context does not contain enough information
   to answer the question, clearly say so.
4. Use previous conversation only to understand
   references such as "he", "she", "it", or "they".
5. Give a clear and concise answer.
"""

    else:

        system_prompt = """
You are Rexa, an AI research assistant.

Your name is Rexa.

You were developed by Taufiq Zahan Tushar.

Answer the user's question using your general knowledge.

IDENTITY RULES:
1. Your name is Rexa.
2. If the user asks "Who are you?", introduce yourself
   as Rexa, an AI research assistant.
3. If the user asks "What is your name?", say that
   your name is Rexa.
4. If the user asks who developed you, say that you
   were developed by Taufiq Zahan Tushar.
5. Do not introduce yourself as ChatGPT.
6. Do not claim that your name is ChatGPT.
7. If the user asks about the underlying model, explain
   that Rexa uses the GPT-OSS-120B model through the
   Groq API.

Use the previous conversation to understand
follow-up questions and references.

Give a clear, accurate and concise explanation.
"""


    messages.append(
        {
            "role": "system",
            "content": system_prompt
        }
    )


    # -----------------------------------------
    # Add conversation history
    # -----------------------------------------

    if chat_history:

        for message in chat_history:

            messages.append(
                {
                    "role": message["role"],
                    "content": message["content"]
                }
            )


    # -----------------------------------------
    # Add document context
    # -----------------------------------------

    if context:

        messages.append(
            {
                "role": "system",
                "content": f"""
DOCUMENT CONTEXT:

{context}
"""
            }
        )


    # -----------------------------------------
    # Add current question
    # -----------------------------------------

    messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    # -----------------------------------------
    # Call Groq
    # -----------------------------------------

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",

        messages=messages,

        temperature=0.3,

        max_completion_tokens=1000,

        top_p=1,

        reasoning_effort="medium"
    )


    return (
        completion
        .choices[0]
        .message
        .content
    )