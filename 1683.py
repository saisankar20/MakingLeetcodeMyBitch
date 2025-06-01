import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    mask  = (tweets["content"].str.len() > 15)

    result = tweets.loc[mask, ["tweet_id"]]

    return result

    
