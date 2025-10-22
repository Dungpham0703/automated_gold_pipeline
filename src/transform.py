import pandas as pd

def transform_data(data):

    if isinstance(data, dict):
        data = [data]

    df = pd.DataFrame(data)

    if "price" in df.columns:
        df["gold"] = df["price"]

    """Adjust time in date column"""
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])

    """Adjust time in timestamp column"""
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms", utc=True)
    
    """Change name XAU to GOLD"""
    df["metal"] = df["metal"].replace({
        "XAU": "GOLD"
    })

    df = df.sort_values("timestamp")

    print("Transformed DataFrame:")

    return df
