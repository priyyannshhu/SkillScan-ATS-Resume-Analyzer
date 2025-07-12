# 🚀 SkillScan - ATS Resume Analyzer

SkillScan is an intelligent ATS Resume Analyzer powered by the Google Gemini API. It helps job seekers evaluate their resumes against job descriptions and provides actionable insights like match scores, skill recommendations, and role fitment.

## ✨ Features

### 🔍 Resume Evaluation
Get HR-style feedback on strengths, weaknesses, and job fit.

### 📈 Skill Recommendations
Discover the top 5 skills/certifications to improve your chances.

### 📊 ATS Match Score
Check your compatibility score and missing keywords from the job description.

### 🧭 Career Guidance
Let AI suggest the best-fit tech role for your background.

### 🎨 Modern UI
Custom Streamlit theme with a responsive dark layout.

## 🛠 Tech Stack

- **Streamlit** - Web framework for the user interface
- **Google Gemini API** - AI-powered analysis engine
- **Python** - Core programming language
- **PyPDF2** - PDF processing library
- **dotenv** - Environment variable management for secure API keys

## 🧑‍💻 Local Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/priyyannshhu/SkillScan-ATS-Resume-Analyzer.git
cd SkillScan-ATS-Resume-Analyzer
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up .env file
Create a file named `.env` in the root directory of the project and add your Google Gemini API key:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 5. Run the app
```bash
streamlit run app.py
```

## 🚀 Deployment on Streamlit Cloud

1. Push your code to a public GitHub repository (e.g., https://github.com/priyyannshhu/SkillScan-ATS-Resume-Analyzer).
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Connect your GitHub repository.
4. Add your environment secret (`GOOGLE_API_KEY`) in the Streamlit Cloud settings for your app.
5. Deploy, and your app will be live!

## 🔐 Environment Variables

Your `.env` file should look like this:
```
GOOGLE_API_KEY=your_api_key_here
```

**Important:** Ensure you never commit `.env` to GitHub. Use `.gitignore` to exclude it.

## 🙌 Credits

👨‍💻 **Built by** [Priyanshu Vishwakarma](https://www.instagram.com/priyyannshhu)  
🤖 **Gemini API integration** inspired by Google's official documentation.

## 🔗 Links

- **Live App:** [SkillScan - ATS Resume Analyzer](https://skillscan-ats-resume-analyzer.streamlit.app)
- **GitHub Repo:** [priyyannshhu/SkillScan-ATS-Resume-Analyzer](https://github.com/priyyannshhu/SkillScan-ATS-Resume-Analyzer)
- **LinkedIn:** [Priyanshu Vishwakarma](https://www.linkedin.com/in/priyanshu-vishwakarmaa/)

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
