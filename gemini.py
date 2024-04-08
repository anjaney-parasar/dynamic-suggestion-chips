import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def chipgenerator(destination):
    model = genai.GenerativeModel("gemini-pro")
    prompt=[f"""
You an expert at making suggestion chips for travel AI chatbots. You get the input
of where the user is travelling to and you generate relevant suggestion chips,
like if a user is booking a flight to Delhi, you would generate three relevant suggestion 
chips like ( comma separated) "What are the transportation options in Delhi?" , "What is the weather like in June in Delhi?",
"Plan a 3 day trip in Delhi"
        
User is planning to go in {destination}, make three relevant suggestion chips.
"""]
    response = model.generate_content(prompt[0], generation_config={"temperature" : 0.4})
    return response.text


