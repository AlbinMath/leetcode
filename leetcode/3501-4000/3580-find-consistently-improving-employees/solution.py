import pandas as pd

def find_consistently_improving_employees(
    employees: pd.DataFrame,
    performance_reviews: pd.DataFrame
) -> pd.DataFrame:

    # Sort reviews by employee and date
    reviews = performance_reviews.sort_values(
        ["employee_id", "review_date"]
    )

    # Keep only employees with at least 3 reviews
    counts = reviews.groupby("employee_id").size()
    eligible = counts[counts >= 3].index

    reviews = reviews[
        reviews["employee_id"].isin(eligible)
    ]

    # Get the latest 3 reviews
    last_three = (
        reviews.groupby("employee_id")
        .tail(3)
        .sort_values(["employee_id", "review_date"])
    )

    # Check strictly increasing ratings
    def check_increasing(group):
        ratings = group["rating"].tolist()
        return ratings[0] < ratings[1] < ratings[2]

    valid_ids = (
        last_three.groupby("employee_id")
        .apply(check_increasing)
    )

    valid_ids = valid_ids[valid_ids].index

    # Keep only improving employees
    valid = last_three[
        last_three["employee_id"].isin(valid_ids)
    ]

    # Calculate improvement score
    scores = (
        valid.groupby("employee_id")["rating"]
        .agg(["first", "last"])
        .reset_index()
    )

    scores["improvement_score"] = (
        scores["last"] - scores["first"]
    )

    # Add names
    result = scores.merge(
        employees,
        on="employee_id",
        how="left"
    )

    # Required ordering
    return result[
        ["employee_id", "name", "improvement_score"]
    ].sort_values(
        ["improvement_score", "name"],
        ascending=[False, True]
    ).reset_index(drop=True)
