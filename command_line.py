# Import the argparse library for parsing command line arguments
import argparse
# Import the requests library for making HTTP requests
import requests

# Define a function to download a file from a given URL and save it with a local filename
def download_file(url, local_filename):
    # Check if the local filename is set to "None"; if so, use the filename from the URL
    if local_filename == "None":
        local_filename = url.split("/")[-1]
    # Make a GET request to the specified URL with streaming enabled
    with requests.get(url, stream=True) as r:
        # Raise an HTTPError for bad responses
        r.raise_for_status()
        # Open a local file with write-binary mode
        with open(local_filename, 'wb') as f:
            # Iterate through the content of the response in chunks of 8192 bytes
            for chunk in r.iter_content(chunk_size=8192):
                # Write each chunk to the local file
                f.write(chunk)
    # Return the local filename for reference or further use
    return local_filename

# Create an ArgumentParser object to handle command line arguments
parser = argparse.ArgumentParser()

# Add a positional argument for the URL of the file to download
parser.add_argument("url", help="Url of the file to download")
# Add an optional argument for specifying the local filename; default is set to None
parser.add_argument("-o", "--output", help="Optional name of the file", default=None)

# Parse the command line arguments
args = parser.parse_args()

# Print the URL and the specified output filename (or None if not provided)
print(args.url)
print(args.output)

# Call the download_file function with the provided URL and output filename
download_file(args.url, args.output)
