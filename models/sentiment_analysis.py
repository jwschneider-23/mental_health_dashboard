#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 19:41:33 2025

@author: jackschneider
"""

from transformers import pipeline
import pandas as pd
import os
os.environ["TRANSFORMERS_NO_TF"] = "1"  # Ensures TensorFlow is disabled

from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    framework="pt"  # <- explicitly tell it to use PyTorch
)

print(classifier("I feel great!"))




def analyze_sentiment(file_path):
    df = pd.read_csv(file_path)
    classifier = pipeline("sentiment-analysis")

    results = classifier(df['title'].tolist())  
    df['sentiment'] = [r['label'] for r in results]
    return df

if __name__ == "__main__":
    df = analyze_sentiment('data/reddit_cleaned.csv')
    df.to_csv('data/reddit_sentiment.csv', index=False)
