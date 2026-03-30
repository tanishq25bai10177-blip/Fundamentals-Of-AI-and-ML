from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data (tiny demo dataset)
items = ["banana peel", "apple core", "plastic bottle", "paper", "battery"]
labels = ["wet", "wet", "recyclable", "dry", "hazardous"]

# Train classifier
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(items)
model = MultinomialNB()
model.fit(X, labels)

# User input
item = input("Enter a waste item name: ")

# Prediction
prediction = model.predict(vectorizer.transform([item]))[0]
print("Predicted Category:", prediction)
