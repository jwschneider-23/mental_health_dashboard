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

print(reddit.user.me())
print('OLA')


reddit = praw.Reddit(
    client_id="JpyGLs2DejwOVf0FI-FwiA",
    client_secret="AKWR_wzr67IFxHl6LP4wN6XCyCmapw",
    user_agent="mental_health_scraper by u/SufficientNumber8454"
)

def fetch_posts(subreddit='mentalhealth', limit=100):
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
