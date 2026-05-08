import os
import sys
import subprocess

# Step 1: Install required packages automatically
def install_packages():
    packages = ["streamlit", "PyPDF2"]
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Step 2: Create app.py automatically if not exists
def create_app():
    if not os.path.exists("app.py"):
        with open("app.py", "w") as f:
            f.write('''
import streamlit as st
import PyPDF2

st.set_page_config(page_title="AI Resume Analyzer")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get skill analysis")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

skills_list = ["Python", "Java", "C++", "Machine Learning", "Data Analysis", "SQL", "HTML", "CSS"]

def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

if uploaded_file:
    text = extract_text(uploaded_file)
    
    st.subheader("📃 Extracted Resume Text")
    st.write(text)

    found_skills = [skill for skill in skills_list if skill.lower() in text.lower()]
    missing_skills = [skill for skill in skills_list if skill not in found_skills]

    st.subheader("✅ Skills Found")
    st.write(found_skills)

    st.subheader("❌ Missing Skills")
    st.write(missing_skills)

    score = int((len(found_skills) / len(skills_list)) * 100)

    st.subheader("📊 Resume Score")
    st.write(f"{score}/100")

    st.subheader("💡 Suggestions")
    if missing_skills:
        st.write("Try adding these skills: " + ", ".join(missing_skills))
    else:
        st.write("Great! Your resume looks strong.")
''')

# Step 3: Run everything
def run_app():
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])

if __name__ == "__main__":
    install_packages()
    create_app()
    run_app()
