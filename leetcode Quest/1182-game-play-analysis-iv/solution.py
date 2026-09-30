import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity["event_date"] = pd.to_datetime(activity["event_date"])

    first_login = (
        activity.groupby("player_id")["event_date"]
        .min()
        .reset_index()
    )

    merged = activity.merge(first_login, on="player_id")

    next_day = merged[
        merged["event_date_x"] ==
        merged["event_date_y"] + pd.Timedelta(days=1)
    ]

    fraction = (
        next_day["player_id"].nunique()
        / first_login["player_id"].nunique()
    )

    return pd.DataFrame({
        "fraction": [round(fraction, 2)]
    })
