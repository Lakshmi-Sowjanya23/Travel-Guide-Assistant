import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------- Load Data ----------
data = pd.read_csv("data/destinations.csv")

# ---------- Vectorization ----------
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data["summary"])

def recommend(user_query, top_n=3):
    query_vec = vectorizer.transform([user_query])
    similarity = cosine_similarity(query_vec, tfidf_matrix)[0]
    
    results = data.copy()
    results["Similarity Score"] = similarity
    results = results.sort_values(by="Similarity Score", ascending=False)
    
    return results.head(top_n)

# ---------- Streamlit UI ----------
st.set_page_config(page_title="Travel Guide Assistant", layout="centered")

st.title("🌍 Travel Guide Assistant")
st.write("Get fast, personalized travel recommendations using compressed destination guides.")

user_input = st.text_input("✍️ Enter your travel preference:", placeholder="beach calm budget")

if user_input:
    recommendations = recommend(user_input)
    st.subheader("✨ Recommended Destinations")
    st.dataframe(recommendations.reset_index(drop=True))
