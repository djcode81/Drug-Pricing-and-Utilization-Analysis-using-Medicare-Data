import pandas as pd
import plotly.express as px

def interactive_outlier_analysis(df):
    # Metrics to analyze
    metrics = ['tot_spndng_2022', 'tot_clms_2022', 'cost_per_claim_2022']

    # Compute cost per claim if not already present
    if 'cost_per_claim_2022' not in df.columns:
        df['cost_per_claim_2022'] = df['tot_spndng_2022'] / df['tot_clms_2022']
        df['cost_per_claim_2022'] = df['cost_per_claim_2022'].fillna(0)  # Handle zero claims

    # Calculate Z-scores for each metric
    for metric in metrics:
        df[f'{metric}_zscore'] = (df[metric] - df[metric].mean()) / df[metric].std()

    # Identify outliers (Z-score threshold: +/- 3)
    df['is_outlier'] = ((df['tot_spndng_2022_zscore'].abs() > 3) |
                        (df['tot_clms_2022_zscore'].abs() > 3) |
                        (df['cost_per_claim_2022_zscore'].abs() > 3))

    # Create an interactive scatterplot
    fig = px.scatter(
        df,
        x='tot_clms_2022',
        y='tot_spndng_2022',
        color='is_outlier',
        hover_data=['brnd_name', 'tot_spndng_2022', 'tot_clms_2022', 'cost_per_claim_2022'],
        labels={'tot_clms_2022': 'Total Claims (2022)', 'tot_spndng_2022': 'Total Spending (2022)'},
        title='Interactive Outlier Analysis: Spending vs Claims (2022)'
    )
    
    # Customize layout
    fig.update_traces(marker=dict(size=8, line=dict(width=1, color='DarkSlateGrey')))
    fig.update_layout(
        legend_title_text='Outlier Status',
        xaxis_title='Total Claims (2022)',
        yaxis_title='Total Spending (2022)',
        template='plotly_white',
        height=600,
        width=900
    )

    # Show the plot
    fig.show()

if __name__ == "__main__":
    # Load the cleaned dataset
    file_path = "/Users/dheerajpv/Documents/Intern/Drug pricing/cleaned_dataset.csv"
    df = pd.read_csv(file_path)
    
    # Perform interactive outlier analysis
    interactive_outlier_analysis(df)
