#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import praw
import pandas as pd
from datetime import datetime, timedelta, timezone
import time

# Set up PRAW with your Reddit application credentials
# Need to replace with your actual credentials
reddit = praw.Reddit(
    client_id='client_id',
    client_secret="client_secret",
    user_agent='user_agent'
)


# When writing this program, I was interested in five years of Reddit posts.
# However, I later learned that querying via the Reddit API is limited to the
# most recent 1,000 records. The scraper still works; it just only returns the last
# 1,000 titles for the queried subreddit
def get_titles_from_subreddit(subreddit_name, years=5):
    
    # Calculate the timestamp for the date five years ago
    time_threshold = datetime.now(timezone.utc) - timedelta(days=years * 365)
    
    
    # Get the subreddit object
    subreddit = reddit.subreddit(subreddit_name)
    
    # Search the posts in the subreddit
    posts = []
    for submission in subreddit.new(limit=None): # Fetching posts
        if submission.created_utc >= time_threshold.timestamp():
            posts.append((datetime.fromtimestamp(submission.created_utc), submission.title))
        else:
            break # Exit loop if a post older than the threshrold is found
            time.sleep(0.65) # Sleep for 0.65 seconds between requests
            
    return posts

def export_titles_to_excel(subreddit, titles, file_name=None):
    if file_name is None:
        file_name = f"{subreddit_name}_underscore_titles.xlsx"
        
    # Convert the list of titles to a DataFrame
    df = pd.DataFrame(titles, columns=['Date', 'Title'])
    
    # Export the DataFrame to an Excel file
    df.to_excel(file_name, index=False)
    
# Specify which subreddit to search; e.g. subreddit_name = 'AskReddit'
subreddit_name = 'subreddit_name'
titles = get_titles_from_subreddit(subreddit_name)
export_titles_to_excel(subreddit_name, titles)
