import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def score_lead(message):

    prompt = f"""
    You are an AI sales assistant.

    Analyze the business lead.

    Return exactly:

    Score: <1-100>

    Category: HOT/WARM/COLD

    Lead:
    {message}
    """

    response = model.generate_content(prompt)

    return response.text