# Mapboxapiscanner

Used for determining whether a leaked/found Mapbox API Key is vulnerable to unauthorized access by other applications or not.

Updated for Python 3, requires [requests](https://requests.readthedocs.io/en/master/) (`pip install requests`).

# Usage

- Clone this Repository
- Run `python MAPBOX_API_SCANNER.py <api-token>`
- Paste API key

> **Script will return API key is vulnerable for XXX API! message and the PoC link/code if determines any unauthorized access within this API key within any API's.**

# API's

- Vector Tiles API
- Raster Tiles API
- Static Images API
- Static Tiles API
- Styles API
- Tilequery API

# To be Included

- Tilesets API
