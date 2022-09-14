import requests
import sys
import warnings

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("api_token")
parser.add_argument("-d", "--domain", default="api.mapbox.com")
args = parser.parse_args()

warnings.filterwarnings("ignore")

apikey = args.api_token

def endpoint_vulnerable(url):
        response = requests.get(url, verify=False)
        return response.status_code == 200

def check_endpoint(url):
    if endpoint_vulnerable(url): print("Vulnerable",[url])
    else: print("Not Vulnerable")


print("Vector Tiles API\t", end="")
url = "https://{}/v4/mapbox.mapbox-streets-v8/1/0/0.mvt?access_token={}".format(args.domain, apikey)
check_endpoint(url)

print("Raster Tiles API\t", end="")
url = "https://{}/v4/mapbox.satellite/1/0/0@2x.jpg90?access_token={}".format(args.domain, apikey)
check_endpoint(url)

print("Static Images API\t", end="")
url = "https://{}/styles/v1/mapbox/streets-v11/static/url-https%3A%2F%2Fwww.mapbox.com%2Fimg%2Frocket.png(-76.9,38.9)/-76.9,38.9,15/1000x1000?access_token={}".format(args.domain, apikey)
check_endpoint(url)

print("Static Tiles API\t", end="")
url = "https://{}/styles/v1/mapbox/streets-v11/tiles/512/1/1/0@2x?access_token={}".format(args.domain, apikey)
check_endpoint(url)

print("Styles API\t\t", end="")
url = "https://{}/styles/v1/examples/cjikt35x83t1z2rnxpdmjs7y7?access_token={}".format(args.domain, apikey)
check_endpoint(url)

print("Tilequery API\t\t", end="")
url = "https://{}/v4/mapbox.mapbox-streets-v8/tilequery/-122.42901,37.80633.json?radius=10&access_token={}".format(args.domain, apikey)
check_endpoint(url)

