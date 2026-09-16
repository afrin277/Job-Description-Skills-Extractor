import streamlit as st
import spacy
import pandas as pd
from pathlib import Path


# -----------------------------------
# Paths
# -----------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "skill_ner_model"


# -----------------------------------
# Load Model
# -----------------------------------

nlp = spacy.load(MODEL_PATH)


# -----------------------------------
# Page Settings
# -----------------------------------

st.set_page_config(
    page_title="Job Skills Extractor",
    page_icon="💼",
    layout="wide"
)


# -----------------------------------
# Title
# -----------------------------------

st.title("💼 Job Description Skills Extractor")

st.write(
    "Extract technical and professional skills "
    "from a job description using NLP and NER."
)


# -----------------------------------
# Input
# -----------------------------------

job_description = st.text_area(
    "Paste Job Description",
    height=250,
    placeholder="Paste a job description here..."
)


# -----------------------------------
# Skill Categories
# -----------------------------------

categories = {

    "Programming": [
        "python", "java", "c", "c++", "javascript",
        "html", "css", "r", "php"
    ],

    "Database": [
        "sql", "mysql", "postgresql", "mongodb",
        "oracle", "database"
    ],

    "AI / ML": [
        "machine learning", "deep learning",
        "artificial intelligence", "nlp",
        "natural language processing",
        "computer vision", "tensorflow",
        "pytorch", "keras", "scikit-learn"
    ],

    "Cloud / DevOps": [
        "aws", "azure", "google cloud",
        "docker", "kubernetes", "jenkins",
        "git", "github", "linux"
    ],

    "Data / BI": [
        "pandas", "numpy", "power bi",
        "tableau", "excel", "matplotlib",
        "statistics"
    ]
}


# -----------------------------------
# Extract Button
# -----------------------------------

if st.button("🔍 Extract Skills"):

    if not job_description.strip():

        st.warning("Please enter a job description.")

    else:

        doc = nlp(job_description)

        skills = []

        for ent in doc.ents:

            if ent.label_ == "SKILL":

                skill = ent.text.strip()

                if skill:
                    skills.append(skill)


        # Remove duplicates
        skills = list(dict.fromkeys(skills))


        # -----------------------------------
        # Results
        # -----------------------------------

        st.subheader("📊 Results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Total Skills Detected",
                len(skills)
            )

        with col2:
            st.metric(
                "Unique Skills",
                len(set(skill.lower() for skill in skills))
            )


        # -----------------------------------
        # Categorize Skills
        # -----------------------------------

        categorized = {}

        for category, category_skills in categories.items():

            found = []

            for skill in skills:

                if skill.lower() in category_skills:
                    found.append(skill)

            if found:
                categorized[category] = found


        # -----------------------------------
        # Display Categories
        # -----------------------------------

        st.subheader("🎯 Skills by Category")

        for category, found_skills in categorized.items():

            st.markdown(f"### {category}")

            st.write(
                " • ".join(found_skills)
            )


        # -----------------------------------
        # All Extracted Skills
        # -----------------------------------

        st.subheader("🧠 All Extracted Skills")

        if skills:

            st.write(
                " • ".join(skills)
            )

        else:

            st.info("No skills detected.")


        # -----------------------------------
        # Simple Chart
        # -----------------------------------

        if categorized:

            chart_data = pd.DataFrame(
                {
                    "Category": list(categorized.keys()),
                    "Skills": [
                        len(x)
                        for x in categorized.values()
                    ]
                }
            )

            st.subheader("📈 Skills Distribution")

            st.bar_chart(
                chart_data.set_index("Category")
            )


        # -----------------------------------
        # Download
        # -----------------------------------

        if skills:

            result_df = pd.DataFrame(
                {"Extracted Skills": skills}
            )

            csv = result_df.to_csv(
                index=False
            )

            st.download_button(
                "⬇️ Download Skills",
                csv,
                "extracted_skills.csv",
                "text/csv"
            )