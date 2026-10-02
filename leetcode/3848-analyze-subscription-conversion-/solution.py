import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    df = user_activity[user_activity["activity_type"] != "cancelled"]

    # Calculate average duration
    grouped = (
        df.groupby(["user_id", "activity_type"])["activity_duration"]
        .mean()
        .add(0.0001)
        .round(2)
        .reset_index()
    )

    # Free trial averages
    trial = (
        grouped[grouped["activity_type"] == "free_trial"]
        .rename(columns={
            "activity_duration": "trial_avg_duration"
        })
        .drop(columns=["activity_type"])
    )

    # Paid averages
    paid = (
        grouped[grouped["activity_type"] == "paid"]
        .rename(columns={
            "activity_duration": "paid_avg_duration"
        })
        .drop(columns=["activity_type"])
    )

    # Keep only users who have BOTH free_trial and paid
    result = trial.merge(
        paid,
        on="user_id",
        how="inner"
    )

    return result.sort_values("user_id").reset_index(drop=True)
