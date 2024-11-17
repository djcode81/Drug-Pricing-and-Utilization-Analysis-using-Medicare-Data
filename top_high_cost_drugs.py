import pandas as pd
import matplotlib.pyplot as plt

def top_high_cost_drugs(df):
    # Group by brand name and calculate total spending for 2022
    top_drugs = df.groupby('brnd_name')['tot_spndng_2022'].sum().nlargest(10)
    
    # Plot the results
    plt.figure(figsize=(12, 6))
    bars = plt.barh(top_drugs.index, top_drugs.values, edgecolor='black')

    # Add data labels
    for bar in bars:
        plt.text(bar.get_width() + 5e10, bar.get_y() + bar.get_height()/2, f'{bar.get_width():.1e}',
                 ha='left', va='center', fontsize=10)

    # Customizations
    plt.title('Top 10 High-Cost Drugs in 2022', fontsize=16, fontweight='bold')
    plt.xlabel('Total Spending (USD)', fontsize=12)
    plt.ylabel('Drug Name', fontsize=12)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=10)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Show plot
    plt.show()

if __name__ == "__main__":
    # Load the cleaned dataset
    file_path = "/Users/dheerajpv/Documents/Intern/Drug pricing/cleaned_dataset.csv"
    df = pd.read_csv(file_path)
    
    # Analyze and visualize top high-cost drugs
    top_high_cost_drugs(df)
