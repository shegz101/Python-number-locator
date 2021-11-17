import phonenumbers

from myNumber import number

from phonenumbers import geocoder

key = '8089378fda4f44a39bba9c564ec1d4ae'

segunNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(segunNumber,"en")
print(yourLocation)

#get service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

# from opencage.geocoder import OpenCageGeocode

# geocoder = OpenCageGeocode(key)

# query = str(yourLocation)

# results = geocoder.geocode(query)

# print(results)