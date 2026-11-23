import pandas as pd

def find_churn_risk_customers(
    subscription_events: pd.DataFrame
) -> pd.DataFrame:

    df = subscription_events.copy()

    # Make sure event_date is datetime
    df['event_date'] = pd.to_datetime(df['event_date'])

    # Sort events chronologically for each user
    df = df.sort_values(
        ['user_id', 'event_date', 'event_id']
    )

    # Aggregate user-level information
    stats = df.groupby('user_id').agg(
        first_date=('event_date', 'min'),
        last_date=('event_date', 'max'),
        max_historical_amount=('monthly_amount', 'max'),
        downgrade_count=(
            'event_type',
            lambda x: (x == 'downgrade').sum()
        ),
        last_event=('event_type', 'last'),
        current_plan=('plan_name', 'last'),
        current_monthly_amount=('monthly_amount', 'last')
    ).reset_index()

    # Days as subscriber
    stats['days_as_subscriber'] = (
        stats['last_date'] - stats['first_date']
    ).dt.days

    # Currently active
    active = stats['last_event'] != 'cancel'

    # Has at least one downgrade
    has_downgrade = stats['downgrade_count'] >= 1

    # Current revenue < 50% of historical maximum
    revenue_drop = (
        stats['current_monthly_amount']
        < 0.5 * stats['max_historical_amount']
    )

    # Subscriber for at least 60 days
    long_enough = stats['days_as_subscriber'] >= 60

    # Apply all conditions
    result = stats[
        active &
        has_downgrade &
        revenue_drop &
        long_enough
    ].copy()

    # Required columns
    result = result[
        [
            'user_id',
            'current_plan',
            'current_monthly_amount',
            'max_historical_amount',
            'days_as_subscriber'
        ]
    ]

    # Required ordering
    result = result.sort_values(
        ['days_as_subscriber', 'user_id'],
        ascending=[False, True]
    ).reset_index(drop=True)

    return result
