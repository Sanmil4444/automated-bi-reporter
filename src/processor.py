import pandas as pd

def clean_data(df):
    df.dropna(inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    return df

def calculate_kpis(df):
    total_revenue = df['revenue'].sum()
    total_leads = df['leads'].sum()
    total_conversions = df['conversions'].sum()

    conversion_rate = (total_conversions / total_leads) * 100 if total_leads else 0

    df_sorted = df.sort_values('date')
    growth_rate = ((df_sorted['revenue'].iloc[-1] - df_sorted['revenue'].iloc[0]) 
                   / df_sorted['revenue'].iloc[0]) * 100

    top_campaign = df.groupby('campaign')['revenue'].sum().idxmax()

    return {
        "total_revenue": round(total_revenue, 2),
        "conversion_rate": round(conversion_rate, 2),
        "growth_rate": round(growth_rate, 2),
        "top_campaign": top_campaign
    }
    
