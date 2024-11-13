from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(text, num_keywords=5):
    """Extract keywords from text using TF-IDF."""
    tfidf = TfidfVectorizer(stop_words='english', max_features=num_keywords)
    tfidf_matrix = tfidf.fit_transform([text])
    keywords = tfidf.get_feature_names_out()
    return keywords

def extract_keywords_from_pdfs(parsed_pdfs):
    """Extract keywords from all parsed PDFs."""
    keywords_dict = {}
    for pdf_name, text in parsed_pdfs.items():
        print(f"Extracting keywords from {pdf_name}...")
        keywords = extract_keywords(text)
        keywords_dict[pdf_name] = keywords
    return keywords_dict

if __name__ == "__main__":
    from pdf_parser import parse_all_pdfs
    parsed_pdfs = parse_all_pdfs()
    keywords_dict = extract_keywords_from_pdfs(parsed_pdfs)
    print("Keyword extraction complete.")
