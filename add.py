import urllib.request
import json

file = open('api_key.txt', 'r')
key = file.read().strip()

origin = 'Woodbridge+VA+22191'
destination = 'Covington+GA+30016'

url = ('https://maps.googleapis.com/maps/api/distancematrix/json'
       + '?language=en-US&units=metric'
       + '&origins={}'
       + '&destinations={}'
       + '&key={}'
       ).format(origin, destination, key)

response = urllib.request.urlopen(url)
response_json = json.loads(response.read())
print(response_json)
# distance_meters = response_json['rows'][0]['elements'][0]['duration']['value']
# distance_minutes = response_json['rows'][0]['elements'][0]['duration']['value'] / 60

# print("Origin: %s\nDestination: %s\nDistance (Meters): %s\nDistance (Seconds): %s"
#       % (origin, destination, distance_meters, round(distance_minutes,2)))



print("Origin :", response_json['origin_addresses'])
print("Destination :",response_json['destination_addresses'])
print("Distance(km) :",response_json['rows'][0]['elements'][0]['distance']['text'])
print("Time(Hr Min) :",response_json['rows'][0]['elements'][0]['duration']['text'])

