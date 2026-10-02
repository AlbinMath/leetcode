import pandas as pd

def find_overbooked_employees(
    employees: pd.DataFrame,
    meetings: pd.DataFrame
) -> pd.DataFrame:

    meetings = meetings.copy()
    meetings["meeting_date"] = pd.to_datetime(meetings["meeting_date"])

    # Get Monday of each week
    meetings["week_start"] = (
        meetings["meeting_date"]
        - pd.to_timedelta(meetings["meeting_date"].dt.weekday, unit="D")
    )

    # Total meeting hours per employee per week
    weekly = (
        meetings.groupby(["employee_id", "week_start"])["duration_hours"]
        .sum()
        .reset_index(name="total_hours")
    )

    # Weeks with more than 20 meeting hours
    heavy = weekly[weekly["total_hours"] > 20]

    # Count heavy weeks per employee
    result = (
        heavy.groupby("employee_id")
        .size()
        .reset_index(name="meeting_heavy_weeks")
    )

    # Keep employees with at least 2 heavy weeks
    result = result[result["meeting_heavy_weeks"] >= 2]

    # Add employee details
    result = result.merge(
        employees,
        on="employee_id",
        how="inner"
    )

    return (
        result[
            ["employee_id", "employee_name", "department", "meeting_heavy_weeks"]
        ]
        .sort_values(
            ["meeting_heavy_weeks", "employee_name"],
            ascending=[False, True]
        )
        .reset_index(drop=True)
    )
