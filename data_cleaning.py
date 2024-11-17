import pandas as pd

def clean_data(file_path, save_path=None):
    df = pd.read_csv(file_path)
    
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(0)
    categorical_cols = df.select_dtypes(include='object').columns
    df[categorical_cols] = df[categorical_cols].fillna('Unknown')
    
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    df.drop_duplicates(inplace=True)
    
    if save_path:
        df.to_csv(save_path, index=False)
        print(f"Cleaned dataset saved to: {save_path}")
    
    return df

if __name__ == "__main__":
    file_path = "/Users/dheerajpv/Documents/Intern/Drug pricing/dataset.csv"
    save_path = "/Users/dheerajpv/Documents/Intern/Drug pricing/cleaned_dataset.csv"
    df_cleaned = clean_data(file_path, save_path)
    print("Cleaned Data Sample:\n", df_cleaned.head())

