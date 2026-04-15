def generate_insights(kpis):
    summary = f"The business generated a total revenue of {kpis['total_revenue']} with a conversion rate of {kpis['conversion_rate']}%. Revenue growth is {kpis['growth_rate']}%."

    if kpis['growth_rate'] > 0:
        insight = "Revenue is increasing, likely due to effective campaigns."
    else:
        insight = "Revenue decline indicates potential issues in marketing or sales."

    if kpis['conversion_rate'] < 10:
        action = "Improve lead quality or optimize conversion funnel."
    else:
        action = "Scale successful campaigns like " + kpis['top_campaign']

    return {
        "summary": summary.strip(),
        "insights": insight,
        "actions": action
    }
