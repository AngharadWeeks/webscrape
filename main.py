import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def planet_number():

    url = 'https://exoplanetarchive.ipac.caltech.edu'
    response = requests.get(url)
    print(response)
    #here successful access yeilds message <Response [200]>

    #makes html into a nice nested tree
    soup = BeautifulSoup(response.text, "html.parser")

    #creates a tag obnject for the first stat object in the html tree
    #The first stat object is the no. confirmed planets
    #to get differet stats you can do selectAll(".stat") and choose which one by indexing
    stats = soup.select_one(".stat")
    #print(stats)

    #format the number correctly so you can do things with it if u want
    num = int(stats.string.strip().replace(',',''))

    if num < 0:
        raise ValueError('Exoplanet number should be >0. Check code :)')
    if num <5000:
        raise ValueError('Exoplanet number should be >5000. Unless some serious invalidation has occured:0. Check code :)')
    return(num)

print(planet_number())






