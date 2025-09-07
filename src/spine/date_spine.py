import pandas as pd

def build_date_spine(start: str, end: str) -> pd.DataFrame:
    """
    Generates a date spine with a comprehensive set of calendar attributes,
    replicating the logic from the original notebook implementation.
    Pure function: no database, no I/O.
    """
    rng = pd.date_range(start=start, end=end, freq="D")
    df = pd.DataFrame({"date": rng})

    # --- PORTED FEATURE ENGINEERING ---
    # Replicating all columns from the original create_date_dimension function.
    
    # Basic date components
    df["date_id"] = df["date"].dt.strftime("%Y%m%d").astype(int)
    df["year"] = df["date"].dt.year
    df["quarter"] = df["date"].dt.quarter
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["day_of_week"] = df["date"].dt.weekday + 1  # 1=Mon..7=Sun
    
    # Name/String representations
    df["day_name"] = df["date"].dt.strftime('%a').str.upper()
    df["month_name"] = df["date"].dt.month_name()
    
    # Composite keys / useful integers
    df["year_month"] = (df["year"] * 100 + df["month"]).astype(int)
    
    # ISO calendar features
    iso_calendar = df["date"].dt.isocalendar()
    df["iso_year"] = iso_calendar["year"].astype(int)
    df["iso_week"] = iso_calendar["week"].astype(int)
    
    # Boolean flags (as integers to match original)
    df["is_weekend"] = (df["day_of_week"] >= 6).astype(int)
    df["is_business_day_generic"] = (df["day_of_week"] < 6).astype(int)

    # --- FINAL COLUMN SELECTION ---
    # The column order is preserved to match the original notebook's 'cols' list.
    final_cols = [
        "date", "date_id", "day_of_week", "day_name", "is_weekend", "year", 
        "quarter", "month", "day", "month_name", "year_month", "iso_year", 
        "iso_week", "is_business_day_generic"
    ]
    
    return df[final_cols]

