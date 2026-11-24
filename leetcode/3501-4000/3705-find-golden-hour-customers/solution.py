import pandas as pd

def find_golden_hour_customers(restaurant_orders: pd.DataFrame) -> pd.DataFrame:
    df = restaurant_orders.copy()

    # Convert timestamp to datetime
    df['order_timestamp'] = pd.to_datetime(df['order_timestamp'])

    # Extract time
    time = df['order_timestamp'].dt.time

    # Peak hours
    lunch_start = pd.to_datetime('11:00:00').time()
    lunch_end = pd.to_datetime('14:00:00').time()
    dinner_start = pd.to_datetime('18:00:00').time()
    dinner_end = pd.to_datetime('21:00:00').time()

    df['is_peak'] = (
        ((time >= lunch_start) & (time < lunch_end)) |
        ((time >= dinner_start) & (time < dinner_end))
    )

    # Aggregate customer statistics
    stats = df.groupby('customer_id').agg(
        total_orders=('order_id', 'count'),
        peak_orders=('is_peak', 'sum'),
        rated_orders=('order_rating', 'count'),
        average_rating=('order_rating', 'mean')
    ).reset_index()

    # Calculate raw peak percentage
    stats['peak_percentage_raw'] = (
        stats['peak_orders'] / stats['total_orders'] * 100
    )

    # Average rating: 2 decimal places
    stats['average_rating'] = (
        stats['average_rating'].round(2)
    )

    # Apply conditions
    result = stats[
        (stats['total_orders'] >= 3) &
        (stats['peak_percentage_raw'] >= 60) &
        (stats['average_rating'] >= 4.0) &
        (
            stats['rated_orders'] / stats['total_orders'] >= 0.50
        )
    ].copy()

    # Peak percentage: 0 decimal places
    result['peak_hour_percentage'] = (
        result['peak_percentage_raw'].round(0).astype(int)
    )

    # Select required columns
    result = result[
        [
            'customer_id',
            'total_orders',
            'peak_hour_percentage',
            'average_rating'
        ]
    ]

    # Sort
    result = result.sort_values(
        by=['average_rating', 'customer_id'],
        ascending=[False, False]
    ).reset_index(drop=True)

    return result
