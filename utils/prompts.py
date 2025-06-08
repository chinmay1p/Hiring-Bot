import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
INTENT_OPTIONS = ["greeting", "info_prompt", "tech_prompt", "tech_questions", "final_resp", "fallback"]

PROMPT_PATH_MAP = {
    "greeting": "prompts/greeting.txt",
    "info_prompt": "prompts/info_prompt.txt",
    "tech_prompt": "prompts/tech_prompt.txt",
    "tech_questions": "prompts/question_prompt.txt",
    "final_resp": "prompts/final_resp.txt",
    "fallback": "prompts/fallback.txt"
}

def get_intent(context):
    conversation = "\n".join(
        [f"{msg['role'].capitalize()}: {msg['content']}" for msg in context]
    )

    classification_prompt = (
        "You are an AI assistant helping classify the next stage of a hiring chatbot conversation.\n\n"
        "This chatbot has the following fixed flow of stages:\n"
        "1. greeting — Greet the candidate and ask if they are ready to proceed.\n"
        "2. info_prompt — Ask for name, email, phone, experience, and location.\n"
        "3. tech_prompt — Ask for their tech stack (languages, frameworks, databases, tools).\n"
        "4. tech_questions — Generate 5 MCQ questions (4 options each) based on the provided tech stack.\n"
        "5. final_response — After all 5 questions are answered, thank the candidate.\n"
        "If the user input doesn't match the expected next step or is unclear, return: fallback.\n\n"
        "Valid return options (exact keyword only): greeting, info_prompt, tech_prompt, tech_questions, final_resp, fallback.\n\n"
        f"Conversation so far:\n{conversation}\n\n"
        "Now return the keyword that represents the next logical stage in the flow (no explanation)."
    )


    payload = {
        "model": "meta-llama/Llama-3-8b-chat-hf",
        "messages": [
            {"role": "system", "content": "You are an intent classification and questions generating assistant."},
            {"role": "user", "content": classification_prompt}
        ],
        "max_tokens": 10,
        "temperature": 0.3,
    }

    try:
        response = requests.post(
            "https://api.together.xyz/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {TOGETHER_API_KEY}",
                "Content-Type": "application/json"
            },
            json=payload
        )
        intent = response.json()['choices'][0]['message']['content'].strip().lower()
        return intent if intent in INTENT_OPTIONS else "fallback"
    except Exception as e:
        print("Together API error:", e)
        return "fallback"

def last_input(context):
    for message in reversed(context):
        if message['role'] == 'user':
            return message['content'].strip()
    return ""

def prompt(context):
    user_input = last_input(context)
    intent = get_intent(context)

    if intent == "tech_questions":
        question_gen_prompt = f"""Based on the candidate's tech stack: {user_input}, generate a total of 5 multiple choice (MCQ) technical questions. Each question must include:
- One question
- Four options (labeled A, B, C, D)
- DO NOT provide the answers.
Questions should be split across all technologies in the tech stack to assess their skills."""
        
        payload = {
            "model": "meta-llama/Llama-3-8b-chat-hf",
            "messages": [
                {"role": "system", "content": "You are an expert technical interviewer and question generator."},
                {"role": "user", "content": question_gen_prompt}
            ],
            "max_tokens": 1024,
            "temperature": 0.7,
        }

        try:
            response = requests.post(
                "https://api.together.xyz/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {TOGETHER_API_KEY}",
                    "Content-Type": "application/json"
                },
                json=payload
            )
            return response.json()['choices'][0]['message']['content'].strip()
        except Exception as e:
            print("Together API error (tech_questions):", e)
            return "Sorry, I couldn't generate questions at the moment."

    
    prompt_path = PROMPT_PATH_MAP.get(intent, PROMPT_PATH_MAP["fallback"])
    template = open(prompt_path).read()
    return template.format(tech_stack=user_input) if "{tech_stack}" in template else template

