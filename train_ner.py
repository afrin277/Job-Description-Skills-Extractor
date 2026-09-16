# ============================================
# Job Description Skills Extractor - NER
# ============================================

import json
import spacy
from pathlib import Path


# --------------------------------------------
# 1. Project paths
# --------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models" / "skill_ner_model"

TRAINING_FILE = DATA_DIR / "ner_training_data.json"


# --------------------------------------------
# 2. Load training data
# --------------------------------------------

if not TRAINING_FILE.exists():
    raise FileNotFoundError(
        "ner_training_data.json not found. Run Notebook 2 first."
    )

with open(TRAINING_FILE, "r", encoding="utf-8") as file:
    training_data = json.load(file)

print("Training data loaded successfully!")
print("Training examples:", len(training_data))


# --------------------------------------------
# 3. Extract unique skills
# --------------------------------------------

skills = set()

for item in training_data:

    text = item.get("text", "")
    entities = item.get("entities", [])

    for entity in entities:

        start = entity[0]
        end = entity[1]
        label = entity[2]

        if label == "SKILL":

            skill = text[start:end].strip().lower()

            if skill:
                skills.add(skill)


print("Unique skill patterns:", len(skills))


# --------------------------------------------
# 4. Remove obvious non-skill words
# --------------------------------------------

invalid_skills = {
    "and", "or", "the", "for", "with",
    "from", "to", "of", "in", "on",
    "a", "an", "is", "are", "be",
    "as", "at", "by",
    "looking for",
    "developer", "developers",
    "job", "jobs",
    "company", "companies",
    "candidate", "candidates",
    "employee", "employees",
    "experience",
    "knowledge",
    "skills",
    "work", "working",
    "university", "college"
}

skills = {
    skill for skill in skills
    if skill not in invalid_skills
}


# --------------------------------------------
# 5. Load English spaCy model
# --------------------------------------------

print("Loading spaCy model...")

nlp = spacy.load("en_core_web_sm")


# --------------------------------------------
# 6. Create EntityRuler
# --------------------------------------------

# Remove old EntityRuler if it exists
if "entity_ruler" in nlp.pipe_names:
    nlp.remove_pipe("entity_ruler")


# Add a fresh EntityRuler
ruler = nlp.add_pipe(
    "entity_ruler",
    before="ner"
)


# --------------------------------------------
# 7. Create patterns
# --------------------------------------------

patterns = []

for skill in skills:

    # Convert skill into lowercase token pattern
    tokens = skill.split()

    pattern = [
        {"LOWER": token}
        for token in tokens
    ]

    patterns.append({
        "label": "SKILL",
        "pattern": pattern
    })


# Longer skills first
patterns.sort(
    key=lambda x: len(x["pattern"]),
    reverse=True
)


# Add patterns
ruler.add_patterns(patterns)

print("SKILL patterns added:", len(patterns))


# --------------------------------------------
# 8. Save model
# --------------------------------------------

MODEL_DIR.parent.mkdir(
    parents=True,
    exist_ok=True
)

nlp.to_disk(MODEL_DIR)

print("NER pipeline saved successfully!")
print("Model location:", MODEL_DIR)


# --------------------------------------------
# 9. Test model
# --------------------------------------------

test_text = """
We are looking for a Python Developer
with experience in Django, SQL, AWS,
Docker and Machine Learning.
"""

print("\nTest Job Description:")
print(test_text)


doc = nlp(test_text)


found_skills = []

for entity in doc.ents:

    if entity.label_ == "SKILL":
        found_skills.append(entity.text)


# Remove duplicates
found_skills = list(dict.fromkeys(found_skills))


print("Extracted Skills:")

if found_skills:

    for skill in found_skills:
        print("-", skill)

else:

    print("No skills found.")


print("\nTraining completed successfully!")