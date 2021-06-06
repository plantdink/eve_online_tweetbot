'''
This is the main module and contains the function that fetches the main population data from the ESI API status endpoint
'''

from tweet_stats import compose_tweet
import requests
import json
import logging
import time

from requests.models import HTTPError
from random_system import get_system_kills, get_system_name
from tweet_stats import compose_tweet, send_tweet


# Final deployment destination is intended to be in a docker container running on a RaspberryPi. Intitally set the logging level to info
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# this function will fetch the current player number and returns the current_population varibale for use by random_system & tweet_stats
def get_current_population():

    # this endpoint requires no auth to fetch data
    endpoint = 'https://esi.evetech.net/latest/status/?datasource=tranquility'
    headers = {'accept': 'application/json', 'Cache-Control': 'no-cache'}

    try:
        response = requests.get(endpoint, headers)
        response.raise_for_status()

        # dev env print statement to check general program progress
        print(f'Population endpoint response: {response.status_code}')

    except HTTPError as http_error:
        print(f'HTTP error occurred with get_curren_population: {http_error}')

    except Exception as err:
        print(f'An error occurred with get_current_population: {err}')
    
    else:
        print('get_current_population request successful')
    
    # this assigns the API response text to the data variable so that you can access the player numbers
    data = json.loads(response.text)
    current_population = data['players']

    # dev env print statement to check API response & general program progress
    print(current_population)

    return current_population


def main():
    while True:

        # this assigns the get_current_population to ciurrent population so that it can be passed to compose_tweet
        current_population = get_current_population()

        system_kills_num, random_system, system_spotlight_stats = get_system_kills()

        system_name, sec_status = get_system_name(random_system)

        tweet = compose_tweet(current_population, system_kills_num, system_name, sec_status, system_spotlight_stats)

        send_tweet(tweet)

        logger.info('Waiting...')
        time.sleep(120)
    

if __name__ == '__main__':
    main()
