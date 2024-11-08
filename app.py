from flask import Flask, request, jsonify
import json
from pydantic import BaseModel, ValidationError
from generate_summary import generate_llm_summary  # Import the LLM function

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Server is running"}), 200

# Define Pydantic model for request validation
class RequestSchema(BaseModel):
    company_name: str
    transcript_text: str



# Endpoint to return summaries
@app.route('/earnings_transcript_summary', methods=['POST'])
def earnings_transcript_summary():
    print("Route accessed")

    data = request.get_json()

     # Validate the incoming data using Pydantic
    try:
        request_data = RequestSchema(**data)
    except ValidationError as e:
        # Return a structured error message if validation fails
        return jsonify({"error": "Invalid input, expects a string", "details": e.errors()}), 400

    try:
        # Call LLM summarization function with provided company name and transcript text
        raw_response = generate_llm_summary(request_data.company_name, request_data.transcript_text)

        # Print the raw response to inspect it
        print("Raw llm response type:" , type(raw_response))
        print("Raw LLM response:", raw_response)

        # The raw response is a string in JSON format
        try:
            summary_dict = json.loads(raw_response.strip("'''"))  # Strip any extra quotes if needed
        except json.JSONDecodeError as e:
            print("Error parsing LLM response:", e)
            return jsonify({"error": "Failed to parse LLM response as JSON"}), 500

        # Access the summary fields from the dictionary
        # If information is not present in document, the default value will be returned
        response = {
            "company_name": summary_dict.get("company_name", "Not mentioned in the document"),
            "financial_performance": summary_dict.get("financial_performance", "Not mentioned in the document"),
            "market_dynamics": summary_dict.get("market_dynamics", "Not mentioned in the document"),
            "expansion_plans": summary_dict.get("expansion_plans", "Not mentioned in the document"),
            "environmental_risks": summary_dict.get("environmental_risks", "Not mentioned in the document"),
            "regulatory_or_policy_changes": summary_dict.get("regulatory_or_policy_changes", "Not mentioned in the document")
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle any exceptions that occur during processing


# Uncomment this if running locally
#if __name__ == '__main__':
#    app.run(host='127.0.0.1', port=5001, debug=True)



