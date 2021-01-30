from typing import List
import praw
import re

if __name__ == "__main__":
    import config
    from DataFileInterface import get_common_stocks
else:
    import data.config as config
    from data.DataFileInterface import get_common_stocks


class RedditInterface:
    reddit = praw.Reddit(client_id = config.reddit_id,
                         client_secret = config.reddit_secret,
                         password = config.reddit_pass,
                         user_agent = config.reddit_user_agent,
                         username = config.reddit_user)

    @staticmethod
    def verify():
        reddit = RedditInterface.reddit
        print(reddit.user.me())

    def get_submissions_for(subreddits: List[str], limit: int):
        subreddit_query = "+".join(subreddits)
        return RedditInterface.reddit.subreddit(subreddit_query).hot(limit=limit)

    @staticmethod
    def find_submissions_stock_symbols(subreddits: List[str], limit: int):
        found_symbols = {}

        stocks = get_common_stocks()

        for submission in RedditInterface.get_submissions_for(subreddits, limit):
            re_results = re.findall("[A-Z]*[-.]?[A-Z][^a-z ]", submission.selftext)

            for re_result in re_results:
                if re_result in stocks:
                    if val := found_symbols.get(re_result):
                        found_symbols[re_result] = val+1
                    else:
                        found_symbols[re_result] = 1

        return found_symbols

if __name__ == '__main__':
    print(RedditInterface.find_submissions_stock_symbols(["wallstreetbets"], 1))