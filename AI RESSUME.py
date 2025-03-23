import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""  # Ensure no NoneType errors
    return text

# Function to rank resumes based on job description
def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()

    job_description_vector = vectors[0]
    resumes_vectors = vectors[1:]

    cosine_similarities = cosine_similarity([job_description_vector], resumes_vectors).flatten()
    return cosine_similarities

# Streamlit App UI
st.set_page_config(page_title="AI Resume Screening", layout="wide")
st.title("📄 AI Resume Screening & Candidate Ranking System")

# Job Description Input
st.subheader("📝 Job Description")
job_description = st.text_area("Enter the job description", height=150)

# Resume Upload Section
st.subheader("📂 Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

# Process and Display Results
if uploaded_files and job_description:
    st.subheader("📊 Ranking Resumes")
    
    resumes = [extract_text_from_pdf(file) for file in uploaded_files]
    
    if any(resumes):  # Ensures at least one resume contains text
        scores = rank_resumes(job_description, resumes)

        # Create DataFrame and sort by ranking score
        results = pd.DataFrame({"Resume": [file.name for file in uploaded_files], "Score": scores})
        results = results.sort_values(by="Score", ascending=False)

        # Display Results in Streamlit Dataframe
        st.dataframe(results.style.format({"Score": "{:.2f}"}).bar(subset=["Score"], color="lightblue"))
    else:
        st.warning("No text could be extracted from the uploaded resumes.")
