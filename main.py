from fastapi import FastAPI
import praw
import random

app = FastAPI()

# Reddit API credentials
reddit = praw.Reddit(
    client_id="w_ARZYgloJW4vjzZsh0j-A",
    client_secret="T2f99AuksLhmeJug_Iyj1fMXkVr6Ew",
    user_agent="redditApi/0.0.1",
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
