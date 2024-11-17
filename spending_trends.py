import pandas as pd
import matplotlib.pyplot as plt

def analyze_spending_trends_with_line(df):
    spending_cols = ['tot_spndng_2018', 'tot_spndng_2019', 'tot_spndng_2020', 'tot_spndng_2021', 'tot_spndng_2022']
    total_spending = df[spending_cols].sum()
    
    years = [col.split('_')[-1] for col in spending_cols] 

    plt.figure(figsize=(12, 6))
    bars = plt.bar(years, total_spending, edgecolor='black')
    plt.plot(years, total_spending, color='black', linestyle='--', marker='o', label='Trend Line')


    for i, bar in enumerate(bars):
        yval = bar.get_height()
        plt.text(i, yval + 5e10, f'{yval:.1e}', ha='center', va='bottom', fontsize=10)

    # Customizations
    plt.title('Total Drug Spending (2018-2022)', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Total Spending (USD)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12) 
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Load the cleaned dataset
    file_path = "/Users/dheerajpv/Documents/Intern/Drug pricing/cleaned_dataset.csv"
    df = pd.read_csv(file_path)
    
    # Analyzing and visualize spending trends with trend line
    analyze_spending_trends_with_line(df)

