import requests
import sys
import warnings

warnings.filterwarnings("ignore")

if len(sys.argv) <= 1:
	print("Usage: python MAPBOX_API_SCANNER.py <api-token>")
	quit()

apikey = sys.argv[1]

def endpoint_vulnerable(url):
	response = requests.get(url, verify=False)
	return response.status_code == 200

print("Vector Tiles API\t", end="")
url = "https://api.mapbox.com/v4/mapbox.mapbox-streets-v8/1/0/0.mvt?access_token="+apikey
if endpoint_vulnerable(url): print("Vulnerable")
else: print("Not Vulnerable")

print("Raster Tiles API\t", end="")
url = "https://api.mapbox.com/v4/mapbox.satellite/1/0/0@2x.jpg90?access_token="+apikey
if endpoint_vulnerable(url): print("Vulnerable")
else: print("Not Vulnerable")

print("Static Images API\t", end="")
url = "https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/url-https%3A%2F%2Fwww.mapbox.com%2Fimg%2Frocket.png(-76.9,38.9)/-76.9,38.9,15/1000x1000?access_token="+apikey 
if endpoint_vulnerable(url): print("Vulnerable")
else: print("Not Vulnerable")

print("Static Tiles API\t", end="")
url = "https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/512/1/1/0@2x?access_token="+apikey 
if endpoint_vulnerable(url): print("Vulnerable")
else: print("Not Vulnerable")

print("Styles API\t\t", end="")
url = "https://api.mapbox.com/styles/v1/examples/cjikt35x83t1z2rnxpdmjs7y7?access_token="+apikey 
if endpoint_vulnerable(url): print("Vulnerable")
else: print("Not Vulnerable")

print("Tilequery API\t\t", end="")
url = "https://api.mapbox.com/v4/mapbox.mapbox-streets-v8/tilequery/-122.42901,37.80633.json?radius=10&access_token="+apikey 
if endpoint_vulnerable(url): print("Vulnerable")
else: print("Not Vulnerable")


