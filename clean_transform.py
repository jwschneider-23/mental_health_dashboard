#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 19:37:37 2025

@author: jackschneider
"""

import pandas as pd

# Load survey data
df_survey = pd.read_csv('data/survey.csv')

# Basic cleaning
df_survey = df_survey[['Age', 'Gender', 'self_employed', 'mental_health_consequence']]
df_survey.dropna(inplace=True)

# Load Reddit data
df_reddit = pd.read_csv('data/reddit_posts.csv')

# Save cleaned versions
df_survey.to_csv('data/survey_cleaned.csv', index=False)
df_reddit.to_csv('data/reddit_cleaned.csv', index=False)
