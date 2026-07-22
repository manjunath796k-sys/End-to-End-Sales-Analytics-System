import os
import pandas as pd


def load_csv(file_path):
    """
    Reads a CSV file using Python file handling
    and loads it into a Pandas DataFrame.
    """

    try:
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Read using Python file handling
        with open(file_path, "r", encoding="utf-8") as file:
            first_line = file.readline()

            if not first_line:
                raise ValueError("CSV file is empty.")

        # Load into Pandas
        df = pd.read_csv(file_path)

        print(f"✔ Successfully loaded {os.path.basename(file_path)}")
        return df

    except FileNotFoundError as error:
        print(error)

    except pd.errors.EmptyDataError:
        print("CSV file contains no data.")

    except Exception as error:
        print(f"Unexpected Error: {error}")

    return None