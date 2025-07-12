import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

# --- Load Keys ---
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# --- App Meta ---
st.set_page_config(page_title="SkillScan - ATS Resume Analyzer", layout="centered")
st.title("SkillScan - ATS Resume Analyzer")
st.caption("Analyze your resume against job descriptions using AI-powered insights")

# --- Inputs ---
input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("✅ Resume uploaded successfully!")

# --- Extract Resume Text ---
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    return "".join([page.extract_text() for page in reader.pages])

# --- Gemini Call ---
def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text

# --- Prompt Templates (Optimized) ---
prompt_template_1 = """
You are a senior HR professional experienced in Data Science, Full Stack Development, DevOps, and Data Analytics roles.
Carefully review the provided resume in the context of the job description.
Provide a detailed, human-readable evaluation of how well the resume matches the job, including key strengths and areas of improvement.
Give:
- 3 key strengths
- 2 weaknesses
- Final verdict: Good match / Partial match / Poor match
Respond in bullet points only.
Do not use any markdown formatting like ** or * around text

Resume:
{text}

Job Description:
{jd}
"""

prompt_template_2 = """
You are a career coach and resume expert. Your task is to scan the resume and suggest the top 5 skills or certifications the candidate should improve or add, based on the job description.
Return the list in bullet points with concise explanations.
Respond in bullet points only. Do not use any markdown formatting like ** or * around text

Resume:
{text}

Job Description:
{jd}
"""

prompt_template_3 = """
You're an intelligent ATS system.
Analyze the resume against the job description and provide a compatibility report.

Return in this format:
Match Score: XX%
Missing Keywords: [list important missing terms]
Summary: Short, structured analysis of alignment

Resume:
{text}

Job Description:
{jd}
"""

prompt_template_4 = """
You're a senior recruiter.
Based on the resume, identify the best-fit role in tech, your confidence score, and reasoning.

Return as:
- Suggested Role
- Confidence Score (%)
- One-line Justification

Resume:
{text}
"""

# --- Button Layout ---
col1, col2 = st.columns(2)
with col1:
    submit1 = st.button("Evaluate Resume")
    submit2 = st.button("Skill Recommendations")
with col2:
    submit3 = st.button("ATS Match Score")
    submit4 = st.button("Career Guidance")

# --- Execution ---
if uploaded_file and input_text.strip():
    resume_text = input_pdf_text(uploaded_file)

    if submit1:
        with st.spinner("Analyzing resume..."):
            prompt = prompt_template_1.format(text=resume_text, jd=input_text)
            st.subheader("📌 Resume Evaluation")
            response_text = get_gemini_response(prompt)
            formatted_response = response_text.replace("\n", "<br>").replace("**", "")
            st.markdown(f"""
            <div style='text-align: left; padding: 1rem; line-height: 1.6; font-size: 1rem;'>
            {formatted_response}
            </div>
            """, unsafe_allow_html=True)

    elif submit2:
        with st.spinner("Generating skill recommendations..."):
            prompt = prompt_template_2.format(text=resume_text, jd=input_text)
            st.subheader("📈 Skill Development Plan")
            response_text = get_gemini_response(prompt)
            formatted_response = response_text.replace("\n", "<br>").replace("**", "")
            st.markdown(f"""
            <div style='text-align: left; padding: 1rem; line-height: 1.6; font-size: 1rem;'>
            {formatted_response}
            </div>
            """, unsafe_allow_html=True)

    elif submit3:
        with st.spinner("Calculating ATS match..."):
            prompt = prompt_template_3.format(text=resume_text, jd=input_text)
            st.subheader("📊 ATS Compatibility Report")
            response_text = get_gemini_response(prompt)
            formatted_response = response_text.replace("\n", "<br>").replace("**", "")
            st.markdown(f"""
            <div style='text-align: left; padding: 1rem; line-height: 1.6; font-size: 1rem;'>
            {formatted_response}
            </div>
            """, unsafe_allow_html=True)

    elif submit4:
        with st.spinner("Analyzing career path..."):
            prompt = prompt_template_4.format(text=resume_text)
            st.subheader("🧭 Career Path Analysis")
            response_text = get_gemini_response(prompt)
            formatted_response = response_text.replace("\n", "<br>").replace("**", "")
            st.markdown(f"""
            <div style='text-align: left; padding: 1rem; line-height: 1.6; font-size: 1rem;'>
            {formatted_response}
            </div>
            """, unsafe_allow_html=True)
else:
    if any([submit1, submit2, submit3, submit4]):
        st.warning("⚠️ Please upload your resume and enter the job description to proceed.")

# --- Footer ---
st.markdown("""
    <div class="footer">
        <p style='font-size:0.9rem;'>
            Built by <strong>Priyanshu Vishwakarma</strong><br>
            <a href='https://github.com/priyyannshhu' target='_blank'>GitHub</a> ·
            <a href='https://www.linkedin.com/in/priyanshu-vishwakarmaa/' target='_blank'>LinkedIn</a> ·
            <a href='https://www.instagram.com/priyyannshhu' target='_blank'>Instagram</a>
        </p>
    </div>
""", unsafe_allow_html=True)



# --- Styles with Your Color Scheme ---
st.markdown("""
    <style>
        html, body, .main, [data-testid="stAppViewContainer"] {
            background-color: #0A1A2F;
            color: #E1EAF5;
            font-family: 'Segoe UI', sans-serif;
        }

        .st-emotion-cache-z5fcl4 {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding-top: 2rem;
        }

        .st-emotion-cache-1oe5zby {
            max-width: 700px;
            width: 100%;
        }

        h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: #E1EAF5;
            text-align: center;
        }

        .stTextArea textarea {
            background-color: #132C4E !important;
            color: #E1EAF5 !important;
            border: 1px solid #2D415F !important;
            border-radius: 8px;
            padding: 12px;
            font-size: 15px;
        }

        .stTextInput>div>div>input {
            background-color: #132C4E !important;
            color: #E1EAF5 !important;
            border: 1px solid #2D415F !important;
            border-radius: 8px;
            padding: 12px;
            font-size: 15px;
        }

        .stFileUploader {
            background-color: #132C4E !important;
            color: #E1EAF5 !important;
            border: 1px solid #2D415F !important;
            border-radius: 8px;
            padding: 8px;
            text-align: center;
        }

        .stButton>button {
            background-color: #2979FF !important;
            color: white !important;
            font-weight: 500;
            font-size: 15px;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
            transition: background-color 0.3s ease;
            width: 100%;
        }

        .stButton>button:hover {
            background-color: #1565C0 !important;
        }

        .stSubheader, .stCaption, .stMarkdown {
            color: #D0DCEC;
            text-align: center;
        }

        hr {
            border: 0;
            height: 1px;
            background: #2D415F;
            margin: 20px 0;
        }

        .stAlert {
            background-color: #1C2B40;
            border: 1px solid #2D415F;
            color: #E1EAF5;
            border-radius: 6px;
            padding: 15px;
        }

        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #0A1A2F;
            color: #D0DCEC;
            text-align: center;
            padding: 12px 0;
            border-top: 1px solid #2D415F;
            font-size: 0.95rem;
        }

        .footer a {
            color: #2979FF;
            text-decoration: none;
            margin: 0 12px;
        }

        .footer a:hover {
            color: #1565C0;
            text-decoration: underline;
        }

        footer {
            visibility: hidden;
        }

        /* Success and warning message styling */
        .stSuccess {
            background-color: #1C2B40;
            border: 1px solid #2D415F;
            color: #E1EAF5;
        }

        .stWarning {
            background-color: #1C2B40;
            border: 1px solid #2D415F;
            color: #E1EAF5;
        }

        /* Spinner styling */
        .stSpinner > div {
            border-top-color: #2979FF !important;
        }
    </style>
""", unsafe_allow_html=True)
