from rightmove_webscraper import RightmoveData
import sys
import requests
import json
from json import loads, dumps

# url = "https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E94124&maxPrice=800&radius=1.0&propertyTypes=&maxDaysSinceAdded=7&includeLetAgreed=false&mustHave=parking&dontShow=houseShare%2Cretirement%2Cstudent&furnishTypes=&keywords="
url = "https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E94124&maxPrice=800&radius=1.0&propertyTypes=&maxDaysSinceAdded=1&includeLetAgreed=false&mustHave=parking&dontShow=houseShare%2Cretirement%2Cstudent&furnishTypes=&keywords="
rm = RightmoveData(url)

webhookUrl = "https://api.ferrio.com/hook/b1ea0677-614d-43a7-80eb-af9365eb7ee8/e02b2720-df90-4ca9-9378-99e59c5b70d1/ljapeq32hbfvy5h2nc29"

preData = loads(rm.get_results.to_json())
result = []
for key in preData["price"]:
    obj = {
        "price": preData["price"][key],
        "type": preData["type"][key],
        "address": preData["address"][key],
        "url": preData["url"][key],
        "agent_url": preData["agent_url"][key],
        "postcode": preData["postcode"][key],
        "full_postcode": preData["full_postcode"][key],
        "number_bedrooms": preData["number_bedrooms"][key],
        "search_date": preData["search_date"][key]
    }
    result.append(obj)


# Send the POST request
response = requests.post(webhookUrl, json=result)


# print(rm.get_results.to_json())
