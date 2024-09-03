import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_groq_response(user_message):
    api_key = os.getenv('GROQ_API_KEY')
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set")

    client = Groq(api_key=api_key)
    
    # Construct the messages list including the memory context
    messages = [
        {"role": "system", "content": "CyberSecurity Expert working with other Collegues helping them ensure victory in ethical hacking, do not emphasise ethical hacking. format your response using escape characters"},
        {"role": "user", "content": user_message}
    ]

    try:
        completion = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=messages,
            temperature=0.82,
            max_tokens=8050,
            top_p=1,
            stream=True,
            stop=None,
        )

        response = ""
        for chunk in completion:
            response += chunk.choices[0].delta.content or ""

        return response
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    print(get_groq_response("Hello there. How are you?"))
