import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    
    mask = ((products["low_fats"] == "Y") & (products["recyclable"] == "Y"))

    result = products.loc[mask, ['product_id']]

    return result
    
