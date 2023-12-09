import json
import pandas as pd

def load_data_from_json(file_path='data.json'):
    with open(file_path, 'r') as file:
        # Load the entire file as a JSON array
        data = json.load(file)

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data)

    return df

if __name__ == "__main__":
    df = load_data_from_json()
    print(df.head())

