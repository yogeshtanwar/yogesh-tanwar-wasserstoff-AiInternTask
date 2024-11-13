import json
import requests
import os

# Path to JSON dataset file
json_file_path = 'data/Dataset.json'

# Directory to save downloaded PDFs
pdf_dir = 'data/pdfs/'

# Create PDF directory if it doesn't exist
os.makedirs(pdf_dir, exist_ok=True)

def download_pdfs():
    # Load JSON data
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    
    for pdf_name, pdf_url in data.items():
        try:
            # Download the PDF
            response = requests.get(pdf_url, stream=True)
            if response.status_code == 200:
                pdf_path = os.path.join(pdf_dir, f"{pdf_name}.pdf")
                with open(pdf_path, 'wb') as pdf_file:
                    pdf_file.write(response.content)
                print(f"{pdf_name}.pdf downloaded successfully.")
            else:
                print(f"Failed to download {pdf_name}.pdf")
        except Exception as e:
            print(f"Error downloading {pdf_name}: {e}")

if __name__ == "__main__":
    download_pdfs()
