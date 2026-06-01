from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

def gold_pipeline():
    df = extract_data("20251011")
    df = transform_data(df)
    load_data(df, "20251011")

if __name__ == "__main__":
    gold_pipeline()
