#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18

script for scraping data from 'mentalhealth' subreddit

@author: jackschneider
"""

import praw
import pandas as pd
from datetime import datetime




reddit = praw.Reddit(
    client_id = "0yfgedB6kJSLTem6tDN3GA",
    client_secret = "8vel5YCqH0ZdfcJC4n-UpPEjHSabjA",
    user_agent = "mental_health_scraper by u/SufficientNumber8454"
)

print(reddit.read_only)
print(reddit.user.me())

def fetch_posts(subreddit='technology', limit=100):
    posts = []
    for post in reddit.subreddit(subreddit).hot(limit=limit):
        posts.append({
            'title': post.title,
            'created': datetime.utcfromtimestamp(post.created_utc),
            'score': post.score,
            'comments': post.num_comments
        })
    return pd.DataFrame(posts)

if __name__ == "__main__":
    df = fetch_posts()
    df.to_csv("data/reddit_posts.csv", index=False)
