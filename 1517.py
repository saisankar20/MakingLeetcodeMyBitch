import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    pat = re.compile(r"^[a-zA-Z][\w\.\-]*@leetcode\.com$", re.IGNORECASE)

    mask =users["mail"].str.fullmatch(pat, na=False)

    result = users.loc[mask, ['user_id','name','mail']]

    return result

    
    
