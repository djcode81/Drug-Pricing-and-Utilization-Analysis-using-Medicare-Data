import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def correlation_analysis(df):
    #relevant columns for correlation
    corr_columns = ['tot_clms_2022', 'tot_spndng_2022', 'avg_spnd_per_clm_2022']
    correlation_data = df[corr_columns]
    
    # Calculating the correlation matrix
    correlation_matrix = correlation_data.corr()
    print("Correlation Matrix:")
    print(correlation_matrix)
    
    # The heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
    plt.title('Correlation Between Claims, Spending, and Costs (2022)', fontsize=16)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Loading the cleaned dataset
    file_path = "/Users/dheerajpv/Documents/Intern/Drug pricing/cleaned_dataset.csv"
    df = pd.read_csv(file_path)
    
    # Performing correlation analysis
    correlation_analysis(df)
