import pandas as pd

def find_books_with_no_available_copies(
    library_books: pd.DataFrame,
    borrowing_records: pd.DataFrame
) -> pd.DataFrame:

    # Keep only currently borrowed books
    current = borrowing_records[
        borrowing_records["return_date"].isna()
    ]

    # Count current borrowers for each book
    borrowers = (
        current.groupby("book_id")
        .size()
        .reset_index(name="current_borrowers")
    )

    # Join with library books
    result = library_books.merge(
        borrowers,
        on="book_id",
        how="inner"
    )

    # Zero copies available:
    # total_copies - current_borrowers = 0
    result = result[
        result["total_copies"] == result["current_borrowers"]
    ]

    # Sort by borrowers DESC, title ASC
    return result[
        [
            "book_id",
            "title",
            "author",
            "genre",
            "publication_year",
            "current_borrowers"
        ]
    ].sort_values(
        ["current_borrowers", "title"],
        ascending=[False, True]
    ).reset_index(drop=True)
