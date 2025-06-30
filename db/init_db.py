#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 19:39:16 2025

@author: jackschneider
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect('db/mental_health.db')

# Store survey
survey = pd.read_csv('data/survey_cleaned.csv')
survey.to_sql('survey', conn, if_exists='replace', index=False)

# Store Reddit
reddit = pd.read_csv('data/reddit_cleaned.csv')
reddit.to_sql('reddit', conn, if_exists='replace', index=False)

conn.close()
