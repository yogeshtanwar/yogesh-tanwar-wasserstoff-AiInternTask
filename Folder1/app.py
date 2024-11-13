# app.py
from fastapi import FastAPI
from src.pdf_parser import parse_all_pdfs

app = FastAPI()

@app.get("/")
def root():
    return {"message": "PDF Summarization API"}

@app.get("/summarize")
def summarize_pdfs():
    # Example route to trigger summarization
    summaries = parse_all_pdfs()
    return {"summaries": summaries}
