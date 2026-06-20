import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# FAQ Data
data = {
    "Question": [
        "What is AI?",
        "What is Python?",
        "Who developed Python?",
        "What is Machine Learning?",
        "What is Streamlit?",
        "What is CodeAlpha?"
    ],
    "Answer": [
        "Artificial Intelligence is the simulation of human intelligence by machines.",
        "Python is a popular high-level programming language.",
        "Python was developed by Guido van Rossum.",
        "Machine Learning is a branch of AI that enables computers to learn from data.",
        "Streamlit is a Python library used to build web applications easily.",
        "CodeAlpha provides internship opportunities and project-based learning."
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["Question"])

st.title("🤖 FAQ Chatbot")
st.write("Ask any question from the FAQ list.")

user_input = st.text_input("Enter your question:")

if st.button("Ask"):

    if user_input.strip() == "":
        st.warning("Please enter a question.")

    else:
        query = vectorizer.transform([user_input])

        similarity = cosine_similarity(query, X)

        index = similarity.argmax()

        answer = df["Answer"][index]

        st.success("Answer:")

        st.write(answer)
