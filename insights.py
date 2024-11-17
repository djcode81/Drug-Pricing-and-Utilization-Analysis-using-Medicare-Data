import pandas as pd

def generate_insights_and_recommendations(df):
    # 1. **Overall Spending Insights**
    total_spending_2022 = df['tot_spndng_2022'].sum()
    top_drug_2022 = df.loc[df['tot_spndng_2022'].idxmax(), 'brnd_name']
    max_spending_2022 = df['tot_spndng_2022'].max()

    # 2. **Top Drugs by CAGR**
    cagr_column = 'cagr_avg_spnd_per_dsg_unt_18_22'
    top_cagr_drugs = df[['brnd_name', cagr_column]].sort_values(by=cagr_column, ascending=False).head(5)

    # 3. **Cost per Claim Analysis**
    cost_per_claim_2022 = 'cost_per_claim_2022'
    df[cost_per_claim_2022] = df['tot_spndng_2022'] / df['tot_clms_2022']
    highest_cost_per_claim = df[['brnd_name', cost_per_claim_2022]].sort_values(by=cost_per_claim_2022, ascending=False).head(5)

    # 4. **Outlier Analysis**
    spending_zscore = (df['tot_spndng_2022'] - df['tot_spndng_2022'].mean()) / df['tot_spndng_2022'].std()
    outliers = df[spending_zscore.abs() > 3]

    # Generate insights
    insights = []
    insights.append(f"1. **Total Spending in 2022:** ${total_spending_2022:,.2f}")
    insights.append(f"2. **Highest Spending Drug in 2022:** {top_drug_2022} with spending of ${max_spending_2022:,.2f}.")
    insights.append("3. **Top 5 Drugs by Compound Annual Growth Rate (CAGR):**")
    for index, row in top_cagr_drugs.iterrows():
        insights.append(f"   - {row['brnd_name']} with CAGR of {row[cagr_column]:.2%}.")
    insights.append("4. **Top 5 Drugs by Cost per Claim (2022):**")
    for index, row in highest_cost_per_claim.iterrows():
        insights.append(f"   - {row['brnd_name']} with an average cost per claim of ${row[cost_per_claim_2022]:,.2f}.")
    insights.append(f"5. **Number of Outlier Drugs (2022 Spending):** {len(outliers)}.")
    insights.append("   - Example Outlier: " + (outliers.iloc[0]['brnd_name'] if len(outliers) > 0 else "None"))

    # Recommendations
    recommendations = []
    recommendations.append("1. **Cost Containment:** Focus on reducing the cost of top outlier drugs to improve affordability.")
    recommendations.append(f"2. **Monitor High-CAGR Drugs:** Monitor drugs with high CAGR, such as {top_cagr_drugs.iloc[0]['brnd_name']}, to manage long-term spending increases.")
    recommendations.append(f"3. **Efficiency Analysis:** Evaluate drugs like {highest_cost_per_claim.iloc[0]['brnd_name']} with high costs per claim to assess their cost-efficiency.")
    recommendations.append("4. **Policy Adjustments:** Consider policies targeting high-spending outliers to regulate overall healthcare costs.")

    # Print Insights and Recommendations
    print("\n--- Insights ---")
    for insight in insights:
        print(insight)
    
    print("\n--- Recommendations ---")
    for recommendation in recommendations:
        print(recommendation)

if __name__ == "__main__":
    # Load the cleaned dataset
    file_path = "/Users/dheerajpv/Documents/Intern/Drug pricing/cleaned_dataset.csv"
    df = pd.read_csv(file_path)
    
    # Generate insights and recommendations
    generate_insights_and_recommendations(df)
