from fastapi import FastAPI
import praw
import random
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()

# Reddit API credentials
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)


@app.get("/random_post")
async def get_random_post(subreddit: str):
    try:
        # Fetch the subreddit
        subreddit_obj = reddit.subreddit(subreddit)

        # Get a random post from the subreddit
        random_post = random.choice(list(subreddit_obj.new(limit=10)))

        # Extract relevant information from the post
        post_info = {
            "title": random_post.title,
            "url": random_post.url,
            "author": random_post.author.name if random_post.author else "Unknown",
        }

        return post_info
    except Exception as e:
        return {"error": str(e)}
