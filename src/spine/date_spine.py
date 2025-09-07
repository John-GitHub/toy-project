import pandas as pd

def build_date_spine(start: str, end: str) -> pd.DataFrame:
    """
    Minimal date spine generator.
    Pure function: no database, no I/O.
    """
    rng = pd.date_range(start=start, end=end, freq="D")
    df = pd.DataFrame({"date": rng})

    # Add useful attributes
    df["day_of_week"] = df["date"].dt.weekday + 1  # 1=Mon..7=Sun
    df["is_weekend"] = df["day_of_week"] >= 6
    df["date_id"] = df["date"].dt.strftime("%Y%m%d").astype(int)

    return df[["date", "date_id", "day_of_week", "is_weekend"]]
