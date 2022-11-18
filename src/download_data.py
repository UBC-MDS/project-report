""" Downloads zip file from the web to a local filepath.
Usage: download_data.py --url=<url> --out_file=<out_file>
Options:
--url=<url>               URL to download data (as zip) from
--out_file=<out_file>     Path (including file name) where to write the file
"""


import requests
import os
from docopt import docopt

opt = docopt(__doc__)

def main(url, out_file):
    
    #check if URL is valid
    try: 
        request = requests.get(url, stream=True)
        request.status_code == 200
    except Exception as ex: 
        print("the URL provided is invalid")
        print(ex)
    
    # save zip file
    with open(out_file, 'wb') as f:
        f.write(request.content)


if __name__ == "__main__":
    main(opt['--url'],opt['--out_file'])