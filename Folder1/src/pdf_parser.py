import os
import PyPDF2

# Directory containing downloaded PDFs
pdf_dir = 'C:/Users/faraz/Downloads/data'

def extract_text_from_pdf(pdf_path):
    """Extract text from a given PDF file."""
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

def parse_all_pdfs():
    """Parse all PDFs in the data/pdfs/ directory and extract their text."""
    parsed_pdfs = {}
    for pdf_name in os.listdir(pdf_dir):
        pdf_path = os.path.join(pdf_dir, pdf_name)
        print(f"Parsing {pdf_name}...")
        text = extract_text_from_pdf(pdf_path)
        parsed_pdfs[pdf_name] = text
    return parsed_pdfs

if __name__ == "__main__":
    pdf_texts = parse_all_pdfs()
    print("PDF Parsing complete.")
