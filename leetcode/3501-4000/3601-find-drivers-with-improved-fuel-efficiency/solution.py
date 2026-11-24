import pandas as pd

def find_improved_efficiency_drivers(
    drivers: pd.DataFrame,
    trips: pd.DataFrame
) -> pd.DataFrame:

    trips = trips.copy()

    # Convert date
    trips["trip_date"] = pd.to_datetime(trips["trip_date"])

    # First half = 1, Second half = 2
    trips["half"] = trips["trip_date"].dt.month.apply(
        lambda x: 1 if x <= 6 else 2
    )

    # Fuel efficiency for each trip
    trips["efficiency"] = (
        trips["distance_km"] / trips["fuel_consumed"]
    )

    # Average efficiency for each driver and half
    avg = (
        trips.groupby(["driver_id", "half"])["efficiency"]
        .mean()
        .reset_index()
    )

    # Convert halves into columns
    avg = avg.pivot(
        index="driver_id",
        columns="half",
        values="efficiency"
    )

    avg = avg.rename(columns={
        1: "first_half_avg",
        2: "second_half_avg"
    })

    # Must have trips in both halves
    avg = avg.dropna()

    # Must actually improve
    avg = avg[
        avg["second_half_avg"] > avg["first_half_avg"]
    ]

    # Improvement
    avg["efficiency_improvement"] = (
        avg["second_half_avg"] - avg["first_half_avg"]
    )

    # Round all numeric results
    avg[
        ["first_half_avg",
         "second_half_avg",
         "efficiency_improvement"]
    ] = avg[
        ["first_half_avg",
         "second_half_avg",
         "efficiency_improvement"]
    ].round(2)

    # Add driver names
    result = avg.reset_index().merge(
        drivers,
        on="driver_id",
        how="inner"
    )

    # Required order
    result = result.sort_values(
        ["efficiency_improvement", "driver_name"],
        ascending=[False, True]
    )

    return result[
        [
            "driver_id",
            "driver_name",
            "first_half_avg",
            "second_half_avg",
            "efficiency_improvement"
        ]
    ].reset_index(drop=True)
