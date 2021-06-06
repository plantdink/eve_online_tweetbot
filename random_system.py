'''
This function will fetch a random systems kill activity, system name and security status. get_system_kills will fetch a list of all systems that have had kill activity registered, select a random system from the list, return system_kills_num, random_system and system_spotlight_stats.
get_system_name will take random_system and return the system_name and sec_status of the system
'''

import requests
import logging
import json
import random

from requests.models import HTTPError

# Final deployment destination is intended to be in a docker container running on a RaspberryPi. Intitally set the logging level to info
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# This willl fetch ALL systems that have had kill activity (usually between 2000 -3000 systems). It selects a random system from the list, returns its kill stats, along with its id for get_system_name
def get_system_kills():

    # this endpoint requires no auth to access
    endpoint = 'https://esi.evetech.net/latest/universe/system_kills/?datasource=tranquility'
    headers = {'accept': 'application/json', 'Cache-Control': 'no-cache'}

    try:
        response = requests.get(endpoint, headers)
        response.raise_for_status()

        # dev env print statement to check response and general program progress
        print(f'System kills response: {response.status_code}')

    except HTTPError as http_error:
        print(f'HTTP error occurred with get_system_kills: {http_error}')

    except Exception as err:
        print(f'An error occurred with get_system_kills: {err}')
    
    else:
        print('get_system_kills request successful')
    
    data = json.loads(response.text)

    #API returns a dict & we want a single random system from that & also need its actual system id number in order to fetch its name details from the systems endpoint
    system_kills_num = len(data)

    # this will pick a random number between 0 and the number of systems with kill activity returned from the API
    random_system_id = random.randint(0, system_kills_num)

    # dev env print to check program progress
    print(f'The system data is {data[random_system_id]}')

    # this is all of the kill data for the random system - it doesn't include its name or security status
    system_spotlight_stats = data[random_system_id]

    # this will get the int value of the random_system_id to be able to fetch the name value using the get_system_name function
    random_system = data[random_system_id]['system_id']

    # dev env print to check program progress
    print(system_kills_num, random_system, system_spotlight_stats)

    return system_kills_num, random_system, system_spotlight_stats


# this function takes random_system_id returned by get_system_kills and fetches its details -system name & security status- from the API to include in the tweet
def get_system_name(random_system):
    system_id = random_system

    # this endpoint require no auth to fetch data from
    endpoint = 'https://esi.evetech.net/latest/universe/systems/' + str(system_id) + '/?datasource=tranquility&language=en'
    headers = {'accept': 'application/json', 'Cache-Control': 'no-cache'}

    try:
        response = requests.get(endpoint, headers)
        response.raise_for_status()

        #dev env print statement to check response & program progress
        print(f'System ID reponse: {response.status_code}')

    except HTTPError as http_error:
        print(f'HTTP error occurred with get_system_name: {http_error}')
    
    except Exception as err:
        print(f'An error occurred with get_system_name: {err}')

    else:
        print('get_system_name request successful')

    # this assigns the API response text to the data variable so that you can access the system details & include them in the tweet body
    data = json.loads(response.text)
    system_name = data['name']
    sec_status = round(data['security_status'], 1)

    # dev env print statement to check values & program progress
    print(f'In {system_name}, the Security Status is {sec_status}.')

    return system_name, sec_status