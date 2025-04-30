import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    for col in df.columns:
        df[col] = df[col].astype('category')
    return df
