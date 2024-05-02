
import requests

def download_file(url, local_filename):
    # Stream the file from the URL and save it locally
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f'Download completed. File saved as {local_filename}')

if __name__ == '__main__':
    # Define the URL of the dataset and the local filename
    dataset_url = 'https://your-dataset-url.com/LoyersMoyen2023.xlsx'  # Update this URL to the actual dataset URL
    local_file_name = 'LoyersMoyen2023.xlsx'
    download_file(dataset_url, local_file_name)
