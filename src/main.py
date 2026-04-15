from data_loader import load_data
from processor import clean_data, calculate_kpis

def run_pipeline():
    df = load_data("../data/sample_data.csv")
    
    if df is None:
        return
    
    df = clean_data(df)
    kpis = calculate_kpis(df)

    print(kpis)

if __name__ == "__main__":
    run_pipeline()
