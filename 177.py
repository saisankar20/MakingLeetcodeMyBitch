import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # 1. unique salaries sorted high → low
    salaries = employee["salary"].drop_duplicates().sort_values(ascending=False)

    # 2. valid N? (must be ≥1 and ≤ number of distinct salaries)
    if 1 <= N <= len(salaries):
        nth_salary = salaries.iloc[N - 1]
    else:
        nth_salary = None                     # → NULL on LeetCode

    # 3. dynamic column name that matches the judge format
    col_name = f"getNthHighestSalary({N})"
    return pd.DataFrame({col_name: [nth_salary]})
