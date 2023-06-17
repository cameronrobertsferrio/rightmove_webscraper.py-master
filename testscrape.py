from rightmove_webscraper import RightmoveData
import sys
import requests
import json

url = "https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E94124&maxPrice=800&radius=1.0&propertyTypes=&maxDaysSinceAdded=1&includeLetAgreed=false&mustHave=parking&dontShow=houseShare%2Cretirement%2Cstudent&furnishTypes=&keywords="
rm = RightmoveData(url)
print(rm.get_results)