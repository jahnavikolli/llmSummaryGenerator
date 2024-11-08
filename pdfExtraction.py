import os
import PyPDF2
import json

# Define the directory containing the PDFs
pdf_directory = "data"

# Paths to the specific PDF files within that directory
pdf_path_1 = os.path.join(pdf_directory, "Earning Call Transcript - Dr Lal Pathlabs.pdf")
pdf_path_2 = os.path.join(pdf_directory, "Earning Call Transcript - One97 (Paytm).pdf")

# Function to extract and clean text from a single PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in range(len(reader.pages)):
            page_text = reader.pages[page].extract_text()
            if page_text:
                # Clean up the extracted text
                page_text = page_text.replace("\n", " ").replace("\r", " ")
                text += page_text
    return text

# Extract and clean text from the PDFs
text_1 = extract_text_from_pdf(pdf_path_1)  # company_name = "Dr Lal Pathlabs"
text_2 = extract_text_from_pdf(pdf_path_2)  # company_name = "One97 (Paytm)"

# Prepare JSON-friendly strings for Postman
json_payload_1 = {
    "company_name": "Dr Lal Pathlabs",
    "transcript_text": text_1
}
json_payload_2 = {
    "company_name": "One97 (Paytm)",
    "transcript_text": text_2
}

# Convert to JSON strings (for easier copying to Postman)
json_str_1 = json.dumps(json_payload_1)
json_str_2 = json.dumps(json_payload_2)

# Print JSON strings for Postman testing
print("JSON Payload for Dr Lal Pathlabs:\n", json_str_1)
#print("\nJSON Payload for One97 (Paytm):\n", json_str_2)
