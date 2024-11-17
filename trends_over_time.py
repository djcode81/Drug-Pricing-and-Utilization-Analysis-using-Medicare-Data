import pandas as pd
import matplotlib.pyplot as plt

def spending_trends_over_time(df):
    # Selecting spending columns for all years
    spending_columns = ['tot_spndng_2018', 'tot_spndng_2019', 'tot_spndng_2020', 'tot_spndng_2021', 'tot_spndng_2022']
    
    # Adding a new column for total spending across all years
    df['total_spending'] = df[spending_columns].sum(axis=1)
    
    # Grouping by brand name and sum total spending
    total_spending_data = df.groupby('brnd_name')[spending_columns].sum()
    
    #top 10 drugs by total spending
    top_spending_drugs = total_spending_data.nlargest(10, 'tot_spndng_2022')
    print("Top 10 Drugs by Spending Trends (2018–2022):")
    print(top_spending_drugs)

    # Plotting trends over time for the top 10 drugs
    plt.figure(figsize=(12, 8))
    for drug in top_spending_drugs.index:
        plt.plot(
            ['2018', '2019', '2020', '2021', '2022'], 
            top_spending_drugs.loc[drug], 
            label=drug, marker='o'
        )

    # Customizations
    plt.title('Spending Trends Over Time (Top 10 Drugs)', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Total Spending (USD)', fontsize=12)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=10)
    plt.legend(title='Drug Name', fontsize=10, title_fontsize=12, loc='upper left')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Loading dataset
    file_path = "/Users/dheerajpv/Documents/Intern/Drug pricing/cleaned_dataset.csv"
    df = pd.read_csv(file_path)
    
    # Performing spending trends analysis
    spending_trends_over_time(df)
