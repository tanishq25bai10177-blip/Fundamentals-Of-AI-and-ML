import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data (very small for demo)
items = ["banana peel", "apple core", "plastic bottle", "paper", "battery"]
labels = ["wet", "wet", "recyclable", "dry", "hazardous"]

# Train simple text classifier
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(items)
model = MultinomialNB()
model.fit(X, labels)

# Streamlit app
st.title("AI-Powered Waste Classifier")
item = st.text_input("Enter a waste item name:")

if item:
    X_test = vectorizer.transform([item])
    prediction = model.predict(X_test)[0]
    st.success(f"Predicted Category: {prediction}")