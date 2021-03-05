import requests
import warnings
import sys

warnings.filterwarnings("ignore")

if len(sys.argv) <= 1:
	print("Usage: python MAPBOX_API_SCANNER.py <api-token>")
	quit()

apikey = sys.argv[1]

url = "https://api.mapbox.com/v4/mapbox.mapbox-streets-v8/1/0/0.mvt?access_token="+apikey 
response = requests.get(url, verify=False)
if response.status_code == 200:
	print("API key is vulnerable for Vector Tiles API! Here is the PoC link which can be used directly via browser:")
	print(url)
else:
	print("API key is not vulnerable for Vector Tiles API.")

url = "https://api.mapbox.com/v4/mapbox.satellite/1/0/0@2x.jpg90?access_token="+apikey
response = requests.get(url, verify=False) 
if response.status_code == 200:
	print("API key is vulnerable for Raster Tiles API! Here is the PoC link which can be used directly via browser:")
	print(url)
else:
	print("API key is not vulnerable for Raster Tiles API.")

url = "https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/url-https%3A%2F%2Fwww.mapbox.com%2Fimg%2Frocket.png(-76.9,38.9)/-76.9,38.9,15/1000x1000?access_token="+apikey 
response = requests.get(url, verify=False)
if response.status_code == 200:
	print("API key is vulnerable for Static Images API! Here is the PoC link which can be used directly via browser:")
	print(url)
else:
	print("API key is not vulnerable for Static Images API.")

url = "https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/512/1/1/0@2x?access_token="+apikey 
response = requests.get(url, verify=False)
if response.status_code == 200:
	print("API key is vulnerable for Static Tiles API! Here is the PoC link which can be used directly via browser:")
	print(url)
else:
	print("API key is not vulnerable for Static Tiles API.")

url = "https://api.mapbox.com/styles/v1/examples/cjikt35x83t1z2rnxpdmjs7y7?access_token="+apikey 
response = requests.get(url, verify=False)
if response.status_code == 200:
	print("API key is vulnerable for Styles API! Here is the PoC link which can be used directly via browser:")
	print(url)
else:
	print("API key is not vulnerable for Styles API.")

url = "https://api.mapbox.com/v4/mapbox.mapbox-streets-v8/tilequery/-122.42901,37.80633.json?radius=10&access_token="+apikey 
response = requests.get(url, verify=False)
if response.status_code == 200:
	print("API key is vulnerable for Tilequery API! Here is the PoC link which can be used directly via browser:")
	print(url)
else:
	print("API key is not vulnerable for Tilequery API.")


