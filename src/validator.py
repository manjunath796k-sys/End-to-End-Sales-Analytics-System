import pandas as pd
from utils import print_header


def validate_data(df, dataset_name):
    """
    Validate the dataset before processing.
    """

    print_header(f"VALIDATING {dataset_name.upper()} DATASET")

    # Dataset Information
    print("\nDataset Information:")
    df.info()

    # Missing Values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Duplicate Records
    duplicates = df.duplicated().sum()
    print(f"\nDuplicate Records: {duplicates}")

    # Data Types
    print("\nData Types:")
    print(df.dtypes)

    print("\nValidation Completed Successfully.")

    return True