#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 19:42:12 2025

@author: jackschneider
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🧠 Mental Health Trends Dashboard")

tab1, tab2 = st.tabs(["Survey Data", "Reddit Trends"])

with tab1:
    df_survey = pd.read_csv("data/survey_cleaned.csv")
    st.subheader("Survey Mental Health Consequences")
    st.bar_chart(df_survey['mental_health_consequence'].value_counts())

with tab2:
    df_reddit = pd.read_csv("data/reddit_sentiment.csv")
    st.subheader("Reddit Sentiment on Mental Health")
    st.write(df_reddit[['title', 'sentiment']].head(10))

    st.subheader("Sentiment Distribution")
    st.bar_chart(df_reddit['sentiment'].value_counts())
