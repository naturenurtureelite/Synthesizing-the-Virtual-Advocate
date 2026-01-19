import google.generativeai as genai

# Configure your API Key
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')

# Dictionary containing the prompt requirements for each language
language_prompts = {
    "Tamil": {
        "context": "Senior Advocate with 20 years experience in India.",
        "style": "Commanding presence, impeccable logic, mastery of Tamil.",
        "task": "Deliver a closing argument regarding a Land Dispute in Tamil."
    },
    "Telugu": {
        "context": "Senior Advocate with 20 years experience in India.",
        "style": "Commanding presence, impeccable logic, mastery of Telugu.",
        "task": "Deliver a closing argument regarding Freedom of Speech in Telugu."
    },
    "Bengali": {
        "context": "Senior Advocate with 20 years experience in Bengali/India.",
        "style": "Commanding presence, impeccable logic, mastery of Bengali.",
        "task": "Deliver a closing argument regarding a Contract Breach in Bengali."
    },
    "Hindi": {
        "context": "Senior Advocate with 20 years experience in India.",
        "style": "Commanding presence, impeccable logic, mastery of Hindi.",
        "task": "Deliver an argument regarding a Criminal Case in Hindi."
    },
    "Gujarati": {
        "context": "Senior Advocate with 20 years experience in India.",
        "style": "Commanding presence, impeccable logic, mastery of Gujarati.",
        "task": "Deliver an argument regarding a Land Dispute in Gujarati."
    }
}

def generate_legal_argument(lang, details):
    prompt = f"""
    Role: You are a {details['context']}
    Traits: {details['style']}
    Task: {details['task']}
    
    Instructions: Use professional legal terminology appropriate for an Indian courtroom. 
    Ensure the tone is authoritative yet respectful to the Bench.
    """
    
    response = model.generate_content(prompt)
    return response.text

# Execute for every language
for lang, details in language_prompts.items():
    print(f"--- Generating Argument for: {lang} ---")
    argument = generate_legal_argument(lang, details)
    print(argument)
    print("\n" + "="*50 + "\n")
