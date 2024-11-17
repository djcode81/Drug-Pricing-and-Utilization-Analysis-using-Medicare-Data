import pandas as pd
import matplotlib.pyplot as plt

def calculate_cagr(start, end, years):
    """Calculate Compound Annual Growth Rate (CAGR)."""
    return ((end / start) ** (1 / years)) - 1 if start > 0 else None

def cagr_analysis(df):
    # Filtering out rows with zero or non-positive spending in 2018
    df = df[df['tot_spndng_2018'] > 0]

    # Selecting relevant columns for analysis
    spending_columns = ['brnd_name', 'tot_spndng_2018', 'tot_spndng_2022']
    cagr_data = df[spending_columns]

    # Calculating CAGR for each drug
    cagr_data['cagr'] = cagr_data.apply(
        lambda row: calculate_cagr(row['tot_spndng_2018'], row['tot_spndng_2022'], 4), axis=1
    )

    # Dropping rows where CAGR is None (to ensure clean data)
    cagr_data = cagr_data.dropna(subset=['cagr'])

    # Get top 10 drugs by CAGR
    top_cagr_drugs = cagr_data.nlargest(10, 'cagr')
    print("Top 10 Drugs by CAGR (2018-2022):")
    print(top_cagr_drugs[['brnd_name', 'tot_spndng_2018', 'tot_spndng_2022', 'cagr']])

    # Plotting the results
    plt.figure(figsize=(12, 6))
    bars = plt.barh(top_cagr_drugs['brnd_name'], top_cagr_drugs['cagr'] * 100, color='skyblue', edgecolor='black')

    # Adding data labels
    for bar in bars:
        plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{bar.get_width():.2f}%',
                 ha='left', va='center', fontsize=10)

    # Customizations
    plt.title('Top 10 Drugs by CAGR (2018-2022)', fontsize=16, fontweight='bold')
    plt.xlabel('CAGR (%)', fontsize=12)
    plt.ylabel('Drug Name', fontsize=12)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=10)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Loading the dataset
    file_path = "/Users/dheerajpv/Documents/Intern/Drug pricing/cleaned_dataset.csv"
    df = pd.read_csv(file_path)
    
    # Performing CAGR analysis
    cagr_analysis(df)

    print(cagr_data.nlargest(10, 'cagr'))

