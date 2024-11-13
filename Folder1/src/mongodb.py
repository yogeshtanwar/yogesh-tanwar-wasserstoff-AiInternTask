from pymongo import MongoClient
import numpy as np

def connect_to_mongodb():
    """Connect to MongoDB and return the collection."""
    client = MongoClient('mongodb://localhost:27017/')
    db = client['pdf_summarization']
    collection = db['summaries']
    return collection

def store_in_mongodb(data):
    """Store data (summaries and keywords) in MongoDB."""
    collection = connect_to_mongodb()
    for pdf_name, details in data.items():
        # Check and convert numpy arrays to Python lists
        if isinstance(details['keywords'], np.ndarray):
            details['keywords'] = details['keywords'].tolist()

        collection.update_one(
            {"pdf_name": pdf_name},
            {"$set": details},
            upsert=True
        )

if __name__ == "__main__":    
    from summarizer import summarize_pdfs
    from keywords import extract_keywords_from_pdfs
    from pdf_parser import parse_all_pdfs

    # Parse, summarize, and extract keywords
    parsed_pdfs = parse_all_pdfs()
    summaries = summarize_pdfs(parsed_pdfs)
    keywords = extract_keywords_from_pdfs(parsed_pdfs)

    # Prepare data to store in MongoDB
    combined_data = {}
    for pdf_name in summaries.keys():
        combined_data[pdf_name] = {
            'summary': summaries[pdf_name],
            'keywords': keywords[pdf_name]
        }

    # Store in MongoDB
    store_in_mongodb(combined_data)
    print("Data stored in MongoDB.")
