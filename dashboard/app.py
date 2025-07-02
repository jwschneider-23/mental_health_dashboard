#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 19:42:12 2025

@author: jackschneider
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Mental Health Trends Dashboard")

tab1, tab2 = st.tabs(["Survey Data", "Reddit Trends"])

with tab1:
    ## Display the tallys of each response from the survey
    fig, ax = plt.subplots()
    df_survey = pd.read_csv("data/survey_cleaned.csv") # read the survey
    column_to_tally = 'mental_health_consequence'
    tally = {"Yes": 0, "No": 0, "Maybe": 0}
    for response in df_survey[column_to_tally]:
        response = str(response).strip().capitalize() # Normalize
        if response in tally:
            tally[response] += 1
    ## Visualize
    labels = list(tally.keys())
    counts = list(tally.values())
    ax.bar(labels, counts, color = 'skyblue')
    ax.set_title("Frequency of Mental Health Consequences")
    ax.set_xlabel("Response", fontweight = 'bold')
    ax.set_ylabel("Count", fontweight = 'bold')
    plt.figtext(0.5,-0.1, "Data taken from OSMI (Open Sourcing Mental Illness) \n The survey was self selected and was spread around online. \n respondents are from various countries including US, Canada, UK, India, and Germany", ha= 'center')
    st.pyplot(plt)
   

with tab2:
    df_reddit = pd.read_csv("data/reddit_sentiment.csv")
    st.subheader("Reddit Sentiment on Mental Health")
    st.write(df_reddit[['title', 'sentiment']].head(10))

    st.subheader("Sentiment Distribution")
    st.bar_chart(df_reddit['sentiment'].value_counts())
