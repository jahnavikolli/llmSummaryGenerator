import os
import time
import typing
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Access your API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    raise ValueError("API Key not set. Please check your environment variables.")

# Define the expected JSON schema using TypedDict
class TranscriptSummary(typing.TypedDict):
    company_name: str
    financial_performance: str
    market_dynamics: str
    expansion_plans: str
    environmental_risks: str
    regulatory_or_policy_changes: str

# Configure the Generative AI model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def generate_llm_summary(company_name, transcript_text):
    # Create the prompt
    prompt = f"""
    Summarize the details from the following transcript text '{transcript_text}' for '{company_name}'
    in short and concise manner, and ensure no repetitive phrases or sentences are included. 
    If any category has no information, return "Not mentioned in the document".
    Return the response in the specified JSON format.
    """

    def generate_with_retry(transcript_text, max_retries=5):
        retries = 0
        while retries < max_retries:
            try:
                result = model.generate_content(
                        prompt,
                        generation_config=genai.GenerationConfig(
                            temperature= 0.3,
                            response_mime_type="application/json",
                            response_schema=TranscriptSummary,
    
                        )
                    )

                # Assuming the result's content is directly in JSON string format
                if hasattr(result, 'candidates') and len(result.candidates) > 0:
                    response_text = result.candidates[0].content.parts[0].text
                    return response_text  # Return the raw JSON string

            except Exception as e:
                retries += 1
                print(f"Error occurred: {e}. Retrying... {retries}/{max_retries}")
                time.sleep(2 ** retries)

        return None


    # Generate a summary for the full transcript
    summary = generate_with_retry(transcript_text)

    if summary:
        print("Full Transcript Summary (Raw LLM Response):", summary)  # Print the raw response
    else:
        print("Failed to process transcript after retries")
    
    return summary
    
    