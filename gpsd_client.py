import json
from gpsdclient import GPSDClient

# get your data as json strings:
with GPSDClient(host="127.0.0.1") as client:
    for result in client.json_stream():
        data = json.loads(result)
        print(data)

# # or as python dicts (optionally convert time information to `datetime` objects)
# with GPSDClient() as client:
#     for result in client.dict_stream(convert_datetime=True, filter=["TPV"]):
#         print("Latitude: %s" % result.get("lat", "n/a"))
#         print("Longitude: %s" % result.get("lon", "n/a"))

# # you can optionally filter by report class
# with GPSDClient() as client:
#     for result in client.dict_stream(filter=["TPV", "SKY"]):
#         print(result)
