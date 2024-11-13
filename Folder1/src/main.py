#ssssssstransformers-env\Scripts\activate

from pdf_parser import parse_all_pdfs
from summarizer import summarize_pdfs
from keywords import extract_keywords_from_pdfs
from mongodb import store_in_mongodb

def run_pipeline():
    # Step 1: Parse PDFs
    parsed_pdfs = parse_all_pdfs()

    # Step 2: Summarize PDFs
    summaries = summarize_pdfs(parsed_pdfs)

    # Step 3: Extract Keywords
    keywords = extract_keywords_from_pdfs(parsed_pdfs)

    # Step 4: Store data in MongoDB
    combined_data = {}
    for pdf_name in summaries.keys():
        combined_data[pdf_name] = {
            'summary': summaries[pdf_name],
            'keywords': keywords[pdf_name]
        }
    store_in_mongodb(combined_data)

if __name__ == "__main__":
    run_pipeline()
    print("Pipeline execution complete.")
