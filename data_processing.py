import pandas as pd

def prepare_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    # Basic cleaning and processing (à améliorer)
    # data.dropna(inplace=True)
    return data
