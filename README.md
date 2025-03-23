AI Resume Screening & Ranking System

📌 Overview

The AI Resume Screening & Candidate Ranking System is a Streamlit-based web application that allows recruiters and hiring managers to upload multiple resumes (in PDF format) and compare them against a given job description. Using TF-IDF vectorization and cosine similarity, the system ranks the resumes based on their relevance to the job description.

🚀 Features

Upload multiple resumes in PDF format

Enter a job description for comparison

AI-based ranking of resumes based on relevance

Interactive Streamlit UI for easy use

Visualization of similarity scores using a ranked table

🔧 Installation & Setup

Prerequisites

Ensure you have Python 3.7+ installed on your system.

1️⃣ Clone the repository:
git clone https://github.com/yourusername/ai-resume-screening.git
cd ai-resume-screening
2️⃣ Install dependencies:
pip install -r requirements.txt
3️⃣ Run the application:
streamlit run AI_RESSUME.py

🛠 Technologies Used

Python 🐍

Streamlit (for UI)

PyPDF2 (for PDF text extraction)

Scikit-learn (TF-IDF and cosine similarity)

Pandas (for data handling)

📷 Screenshots

Add screenshots here to showcase the UI and results.

📜 How It Works

The user enters the job description.

The user uploads multiple PDF resumes.

The system extracts text from resumes using PyPDF2.

TF-IDF vectorization converts text into numerical data.

Cosine similarity compares resumes with the job description.

Resumes are ranked based on their similarity scores.

Results are displayed in a sortable dataframe.

💡 Future Improvements

Support for multiple job descriptions.

NLP-based semantic matching.

More robust PDF text extraction.

Candidate profile analysis.

🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

📜 License

This project is open-source and available under the MIT License.

👨‍💻 Developed by Chelikani Harshal
