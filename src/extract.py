from src.config import GOLD_API_URL, GOLD_API_KEY
import asyncio
import aiohttp
import pandas as pd
from datetime import datetime

async def extract_data_async(date_str=None):
    if date_str is None:
        date_str = datetime.now().strftime("%Y%m%d")  

    url = f"{GOLD_API_URL}/{date_str}"

    headers = {
        "x-access-token": GOLD_API_KEY,
        "Content-Type": "application/json"
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as res:
            res.raise_for_status()
            data = await res.json()

    df = pd.DataFrame([data])
    print(df)
    print(f"Extracted {len(df)} row(s) from {url}")
    return df

def extract_data(date_str=None):
    return asyncio.run(extract_data_async(date_str))
