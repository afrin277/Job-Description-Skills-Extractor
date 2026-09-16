# 💼 Job Description Skills Extractor

An NLP-based application that automatically extracts important skills from job descriptions using Named Entity Recognition (NER) and provides a simple visual analysis through Streamlit.

## 📌 Project Overview

Recruiters and job seekers often need to identify technical skills from large job descriptions. Manually reading and extracting these skills can be time-consuming.

This project uses Natural Language Processing (NLP) to automatically identify skills such as Python, SQL, Machine Learning, AWS, Docker, Django and other technical skills from job descriptions.

The extracted skills are displayed through an interactive Streamlit application along with skill counts, categories and a simple visualization.

## 🎯 Objectives

- Clean and preprocess job-related data.
- Perform exploratory data analysis (EDA).
- Prepare skill-based NER data.
- Extract skills from job descriptions.
- Categorize extracted skills.
- Evaluate the skill extraction pipeline.
- Build an interactive Streamlit application.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- spaCy
- Natural Language Processing (NLP)
- Named Entity Recognition (NER)
- EntityRuler
- Matplotlib
- Streamlit
- Jupyter Notebook
- Git & GitHub

## 📂 Project Structure

```text
NLP_PROJECT/
│
├── app/
│   └── app.py
│
├── data/
│   ├── clean_jobs.csv
│   ├── evaluation_results.json
│   ├── jobs.csv
│   ├── ner_prediction_results.csv
│   ├── ner_training_data.json
│   └── skill_dictionary.json
│
├── models/
│   └── skill_ner_model/
│
├── notebooks/
│   ├── 01_data_cleaning_and_eda.ipynb
│   ├── 02_ner_skill_extraction.ipynb
│   └── 03_testing_and_evaluation.ipynb
│
├── README.md
├── requirements.txt
├── train_ner.py
├── .gitignore
└── venv/
```

## 🔄 Project Workflow
Job Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Skill Extraction & NER Data Preparation
     ↓
NER Skill Patterns
     ↓
spaCy NER Pipeline
     ↓
Skill Extraction
     ↓
Evaluation
     ↓
Streamlit Application

## 🧠 NER Skill Extraction

The project uses spaCy's EntityRuler to identify skill entities from job-related text.

Skills are assigned the entity label:

SKILL

## For example:

Python
SQL
AWS
Docker
Django
Machine Learning

## A sample job description such as:

Looking for a Python Developer with experience
in Django, SQL, AWS, Docker and Machine Learning.

## can produce:

Python
Django
SQL
AWS
Docker
Machine Learning

## 📊 Streamlit Application

**The application allows users to:**

Paste a job description.
Extract skills automatically.
View the total number of detected skills.
View skills grouped into categories.
View a simple skills distribution chart.
Download the extracted skills as a CSV file.

## 📓 Notebooks

**01 - Data Cleaning and EDA**
**Contains:**

Dataset loading
Data inspection
Missing-value handling
Text cleaning
Skill preprocessing
Exploratory data analysis

**02 - NER Skill Extraction**
**Contains:**

Skill extraction
NER training-data preparation
Skill dictionary creation
EntityRuler preparation
NER pipeline creation

**03 - Testing and Evaluation**
**Contains:**

Model loading
Skill extraction testing
Evaluation
Prediction results
Manual test cases

## ▶️ How to Run the Project

**1. Clone the repository**
git clone https://github.com/afrin277/Job-Description-Skills-Extractor.git

**2. Open the project**
cd Job-Description-Skills-Extractor

**3. Create a virtual environment**
python -m venv venv

**4. Activate the virtual environment**
**Windows:**
venv\Scripts\activate

**5. Install dependencies**
pip install -r requirements.txt

**6. Run the Streamlit application**
streamlit run app/app.py

## 📈 Sample Skills
The application can identify skills such as:

Python
Java
SQL
MySQL
MongoDB
Django
Flask
JavaScript
React
Machine Learning
Deep Learning
NLP
TensorFlow
PyTorch
AWS
Azure
Docker
Kubernetes
Git
Power BI
Excel

## 📦 Dataset
The project uses the Jobs on Naukri.com dataset available on **Kaggle.**

**Dataset source:**
https://www.kaggle.com/datasets/promptcloud/jobs-on-naukricom

The raw and intermediate dataset files are excluded from this repository using .gitignore because of their file size.

## ⚠️ Evaluation Note
The current evaluation compares extracted skills with the skills available in the dataset.

Since the EntityRuler patterns are derived from the available skill data, this evaluation should not be interpreted as performance on a completely unseen, independently annotated test set.

## 🚀 Future Improvements
Use a larger manually annotated NER dataset.
Train a statistical NER model.
Improve skill normalization.
Improve skill categorization.
Add resume-to-job skill matching.
Deploy the Streamlit application online.

## 👩‍💻 Author
Afrin

⭐ If you find this project useful, feel free to explore the repository.

### Then save it.

Now in your terminal run:

```powershell
git status

You should see:

modified: README.md

Then run:

git add README.md

Then:

git commit -m "Add project documentation"

And finally:

git push

After that, refresh your GitHub repository page. Your README should automatically appear on the front page.
```

**One small note:** I deliberately described your current approach as spaCy EntityRuler-based NER/entity recognition, rather than claiming you've trained a statistical NER model. That's technically more accurate and will make your project explanation stronger in an interview. ❤️
