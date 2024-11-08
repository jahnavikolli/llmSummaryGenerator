# llmSummaryGenerator


### Explanation of Each Section:
- **Clone the Repository**
- **Set Up a Virtual Environment**:
On Windows:
```
python -m venv venv
venv\Scripts\activate
```
- **Install Dependencies**: Install the required Python packages using `requirements.txt`.
- **Set Up Environment Variables**: Generate GEMINI API KEY to utilize Gemini 1.5 Flash LLM Model. And add it to your `.env` file.
- **Run the Flask Application**: Run the Flask app with the development server or Gunicorn for production. If running on development server uncomment the ```app.run()``` function and ```if ___main___ ===``` line.
- **Extract PDF text**: Upload your file into data folder and access it through its path to extract the text compatable to send as JSON
- **Access the API**: Send a POST request on `/earnings_transcript_summary'` endpoint.
- **Input Structure**: Send a POST request in the following JSON format
  ```
  {
    "company_name": "company_name", 
    "transcript_text": "extracted_text_from_pdf"
  }
  ```
- **Output Structure**:
```
{
  "company_name": "Reliance Industries",
  "financial_performance": "SHORT SUMMARY OF FINANCIAL PERFORMANCE",
  "market_dynamics": "SHORT SUMMARY OF MARKET DYNAMICS",
  "expansion_plans": "SHORT SUMMARY OF EXPANSION PLANS",
  "environmental_risks": "SHORT SUMMARY OF ENVIRONMENTAL RISKS",
  "regulatory_or_policy_changes": "SHORT SUMMARY OF REGULATORY OR POLICY CHANGES"

}
```
- **Stopping the Application**: Enter ``` ctrl+C ``` to stop the server.  


Project Summary
Purpose: The API is designed to extract and summarize important information from earnings call transcripts of various companies. It aims to provide structured insights, such as key financial highlights, strategic updates, and regulatory information, which can be useful for investors and analysts.

-Technologies Used:

-Backend Framework: Flask is used to create the API endpoints.
-Large Language Model (LLM): The project uses Gemini 1.5 Flash for natural language processing and summarization.
-PDF Handling: The project involves extracting text from PDFs, which contain earnings call details.
-Token Management: Careful chunking of text ensures that the API efficiently handles the LLM’s token limit of 12,000 tokens.

Workflow:

Users send a POST request to the /earnings_transcript_summary endpoint, providing the company name and the text of the transcript.
The text is split into manageable chunks, if necessary, to respect the LLM's token constraints.
The LLM processes the text and returns a structured JSON response with specific fields (e.g., financial performance, future outlook, etc.).
Summaries are compiled from individual chunk responses to produce a cohesive output.

-**Features**:

Consistency Handling: The project addresses inconsistencies in LLM responses to ensure that important information is correctly captured.
Structured JSON Output: The API delivers a well-organized response, making it easier to interpret and use for analysis.
Deployment:

Challenges Addressed:

Handling inconsistencies in LLM-generated summaries by refining the prompt and managing tokens efficiently.
Generating a JSON format summary for each fields using LLM
Managing large text data with a structured approach to ensure the API remains performant and within the LLM’s limits.
