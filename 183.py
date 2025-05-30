import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = customers.merge( orders, how='left',left_on='id', right_on='customerId')
    #return merged

    mask = (merged["id_y"].isna())

    result = merged.loc[mask, ['name']].rename(columns={'name':'Customers'})

    return result
