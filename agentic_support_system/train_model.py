# ==========================================================
# train_model.py
# Step 1 Upgrade: Ticket Priority Prediction ML Model
# ==========================================================

import pandas as pd
import sqlite3
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# ----------------------------------------------------------
# FILE PATHS
# ----------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "support_system.db")
MODEL_PATH = os.path.join(BASE_DIR, "priority_model.pkl")

# ----------------------------------------------------------
# LOAD DATA FROM DATABASE
# ----------------------------------------------------------

conn = sqlite3.connect(DB_PATH)

query = """
SELECT issue, priority
FROM tickets
WHERE issue IS NOT NULL
AND priority IS NOT NULL
"""

df = pd.read_sql_query(query, conn)
conn.close()

# ----------------------------------------------------------
# CHECK DATA
# ----------------------------------------------------------

print("Loaded Records:", len(df))
print(df.head())

if len(df) < 5:
    print("Not enough data to train model.")
    exit()

# ----------------------------------------------------------
# FEATURES & LABELS
# ----------------------------------------------------------

X = df["issue"]
y = df["priority"]

# ----------------------------------------------------------
# TRAIN TEST SPLIT
# ----------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# ----------------------------------------------------------
# MACHINE LEARNING PIPELINE
# ----------------------------------------------------------

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

# ----------------------------------------------------------
# TRAIN MODEL
# ----------------------------------------------------------

model.fit(X_train, y_train)

# ----------------------------------------------------------
# TEST MODEL
# ----------------------------------------------------------

predictions = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, predictions))
print("\nReport:\n")
print(classification_report(y_test, predictions))

# ----------------------------------------------------------
# SAVE MODEL
# ----------------------------------------------------------

joblib.dump(model, MODEL_PATH)

print("\nModel Saved Successfully:")
print(MODEL_PATH)