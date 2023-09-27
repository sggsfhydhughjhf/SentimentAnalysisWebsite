import streamlit as st  
import pandas as pd
st.title("Sentiment Analyser:")
import nltk
nltk.download("vader_lexicon")

from nltk.sentiment.vader import SentimentIntensityAnalyzer

file = st.text_input("Enter")
Analyser = SentimentIntensityAnalyzer()

Scores = Analyser.polarity_scores(file)

maximum = pd.DataFrame([Scores]).T.max()[0]
for i in Scores:
    if Scores[i] == maximum:
        result = i
if st.button("Analyze"):
    if result == "neu":
        st.success("neutral")
    elif result == "pos":
        st.success("Positive")
    elif result == "Compound":
        st.success("Compound")
    else:
        st.success("Negative")

