from data_loader import load_data
from processor import clean_data, calculate_kpis
from insight_engine import generate_insights
from reporter import save_report

def run_pipeline():
    df = load_data("../data/sample_data.csv")

    if df is None:
        return

    df = clean_data(df)
    kpis = calculate_kpis(df)
    insights = generate_insights(kpis)

    print("\n===== KPI =====")
    print(kpis)

    print("\n===== AI REPORT =====")
    print(insights)

    save_report(insights, "../output/report.json", "../output/report.txt")

if __name__ == "__main__":
    run_pipeline()
    
