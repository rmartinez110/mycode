#!/usr/bin/python3
import requests
import json

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")

    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate = "start_date=2019-11-11"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)
    # strip off json attachment from our response
    neodata = neowrequest.json()

    largest = {"name": "", "size": 0}
    fastest = {"name": "", "speed": 0}

    for dateGroup in neodata['near_earth_objects']:
        for rock in neodata['near_earth_objects'][dateGroup]:
            if (rock['estimated_diameter']['feet']['estimated_diameter_max'] > largest['size']):
                largest = {"name": rock['name'], "size": rock['estimated_diameter']['feet']['estimated_diameter_max']}
            if (rock['estimated_diameter']['feet']['estimated_diameter_max'] > largest['size']):
                fastest = {"name": rock['name'], "size": rock['estimated_diameter']['feet']['estimated_diameter_max']}

    print(f"Largest Rock:")
    print(largest)



    ## display NASAs NEOW data
    # print(neodata['near_earth_objects']['2019-11-18'][0]['estimated_diameter']['feet']['estimated_diameter_max'])
    

if __name__ == "__main__":
    main()

