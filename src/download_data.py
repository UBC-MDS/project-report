""" Downloads zip file from the web and saves contents to a local directory.
Usage: download_data.py --url=<url> --out_dir=<out_dir>
Options:
--url=<url>             URL to download data (as zip) from
--out_dir=<out_dir>     Path to write the unziped contents to 
"""


import requests
from docopt import docopt
from zipfile import ZipFile
from io import BytesIO

opt = docopt(__doc__)

def main(url, out_dir):
    
    #check if URL is valid
    try: 
        request = requests.get(url, stream=True)
        request.status_code == 200
    except Exception as ex: 
        print("the URL provided is invalid")
        print(ex)
    
    # unzip and save contents
    with ZipFile(BytesIO(request.content)) as zip_file_object:
        zip_file_object.extractall(out_dir)


if __name__ == "__main__":
    main(opt['--url'],opt['--out_dir'])