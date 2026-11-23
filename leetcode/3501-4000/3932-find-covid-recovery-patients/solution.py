import pandas as pd

def find_covid_recovery_patients(
    patients: pd.DataFrame,
    covid_tests: pd.DataFrame
) -> pd.DataFrame:

    # Convert test_date to datetime
    tests = covid_tests.copy()
    tests["test_date"] = pd.to_datetime(tests["test_date"])

    # First positive test for each patient
    positive = (
        tests[tests["result"] == "Positive"]
        .groupby("patient_id")["test_date"]
        .min()
        .reset_index(name="positive_date")
    )

    # Merge positive date back with all tests
    tests = tests.merge(
        positive,
        on="patient_id",
        how="inner"
    )

    # Negative tests after the first positive
    negative = tests[
        (tests["result"] == "Negative") &
        (tests["test_date"] > tests["positive_date"])
    ]

    # First negative after positive
    negative = (
        negative.groupby("patient_id")["test_date"]
        .min()
        .reset_index(name="negative_date")
    )

    # Combine positive and negative dates
    result = positive.merge(
        negative,
        on="patient_id",
        how="inner"
    )

    # Calculate recovery time
    result["recovery_time"] = (
        result["negative_date"] - result["positive_date"]
    ).dt.days

    # Add patient information
    result = result.merge(
        patients,
        on="patient_id",
        how="left"
    )

    # Required output and sorting
    return result[
        [
            "patient_id",
            "patient_name",
            "age",
            "recovery_time"
        ]
    ].sort_values(
        ["recovery_time", "patient_name"],
        ascending=[True, True]
    ).reset_index(drop=True)
