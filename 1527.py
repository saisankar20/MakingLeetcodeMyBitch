import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    mask = patients["conditions"].str.contains(r'(^| )DIAB1', na=False)

    return patients.loc[mask, ["patient_id", "patient_name", "conditions"]]
