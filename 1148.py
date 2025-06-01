import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:

    mask = (views["author_id"] == views["viewer_id"])

    result = views.loc[mask , ["author_id"]].rename(columns={"author_id":"id"}).drop_duplicates().sort_values("id")

    return result
    
