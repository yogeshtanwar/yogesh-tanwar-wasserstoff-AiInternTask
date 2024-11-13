import torch
from transformers import pipeline

# Check if GPU is available and use it
device = 0 if torch.cuda.is_available() else -1

# Option to choose a faster, smaller model like 't5-small' for faster execution
# You can switch back to 'facebook/bart-large-cnn' if you need higher accuracy
summarizer = pipeline("summarization", model="t5-small", device=device)

def summarize_text(text, max_chunk_size=512):
    """Summarize the given text by splitting it into manageable chunks."""
    # Split the text into smaller chunks of max_chunk_size
    text_chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    summaries = []

    # Summarize each chunk and collect summaries
    for chunk in text_chunks:
        summary = summarizer(chunk, max_length=100, min_length=30, do_sample=False)
        summaries.append(summary[0]['summary_text'])

    # Combine all the chunk summaries into one text
    combined_summary = ' '.join(summaries)
    return combined_summary

def summarize_pdfs(parsed_pdfs):
    """Summarize all parsed PDFs."""
    summarized_pdfs = {}
    for pdf_name, text in parsed_pdfs.items():
        print(f"Summarizing {pdf_name}...")
        summary = summarize_text(text)
        summarized_pdfs[pdf_name] = summary
    return summarized_pdfs

if __name__ == "__main__":
    # Assume parsed_pdfs is obtained from the parser
    from pdf_parser import parse_all_pdfs  
    parsed_pdfs = parse_all_pdfs()
    
    # Perform summarization
    summarized_pdfs = summarize_pdfs(parsed_pdfs)
    
    # Output summarization results
    for pdf_name, summary in summarized_pdfs.items():
        print(f"Summary for {pdf_name}:")
        print(summary)
    
    print("Summarization complete.")
