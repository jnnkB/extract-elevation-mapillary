import json
import os
import sys
import time

import requests
from geojson import Feature
from geojson import FeatureCollection


if __name__ == "__main__":
    print("Requesting data… ", end="")
    res = requests.get(
        "https://graph.mapillary.com/images",
        params={
            "sequence_ids": sys.argv[1],
            "fields": "altitude,geometry",
            "access_token": os.environ["MAPILLARY_ACCESS_TOKEN"],
        },
    )
    print("Done")

    print("Transforming data… ", end="")
    data = res.json()["data"]
    data = [
        Feature(geometry=image["geometry"], properties={"altitude": image["altitude"]})
        for image in data
    ]
    print("Done")

    print("Saving data… ", end="")
    with open(f"data/altitude-{time.time()}.geojson", "w") as f:
        json.dump(FeatureCollection(data), f)
    print("Done")
