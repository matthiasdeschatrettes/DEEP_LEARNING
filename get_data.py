import pandas as pd

def download_data(url):
    df = pd.read_csv(url)
    df.to_csv('Base_OP_2023_Nationale.csv', index=False)

if __name__ == "__main__":
    data_url = 'https://www.observatoires-des-loyers.org/datagouv/2023/Base_OP_2023_Nationale.csv'
    download_data(data_url)
