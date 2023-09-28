import csv
import sys

import geojson
import requests

session = requests.Session()
base_url = "https://api.open-meteo.com/v1/elevation"

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = geojson.load(f)

    with open("data/evaluation.csv", "w", newline="") as f:
        fieldnames = [
            "longitude",
            "latitude",
            "open-meteo-elevation",
            "mapillary-altitude",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()

        for feature in data["features"]:
            longitude, latitude = feature["geometry"]["coordinates"]
            res = session.get(
                base_url,
                params={
                    "longitude": longitude,
                    "latitude": latitude,
                },
            )
            elevation = res.json()["elevation"][0]

            writer.writerow(
                {
                    "longitude": longitude,
                    "latitude": latitude,
                    "open-meteo-elevation": elevation,
                    "mapillary-altitude": feature["properties"]["altitude"],
                }
            )
