'''
This module will take the returns from population_check and random_system and send a tweet with the current player count on the Tranquility server, as well as a random system name, kill count & secrity status details
'''

import logging

from tweet_config import create_twitter_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# this will take the current_population from get_current_population, system_kills_num & system_spotlight_stats from get_system_kills, and system_name & sec-status from get_system_name and compose them into a tweet
def compose_tweet(current_population, system_kills_num, system_name, sec_status, system_spotlight_stats):

    # this will sum up the individual NPC, pod & ship kills in the system to give an overall kill count
    spotlight_kills = int(system_spotlight_stats['npc_kills']) + int(system_spotlight_stats['pod_kills']) + int(system_spotlight_stats['ship_kills'])

    logger.info('Composing tweet')

    # below the tweet is constructed from each of the different variables collected
    tweet = (f'Tranquility current player numbers: {current_population} capsuleers. There have been kills in {system_kills_num} systems and in {system_name}, where the security status is {sec_status}, there have been {spotlight_kills} kills in total. #eveonline #tweetfleet')

    # dev env print statement to check tweet structure
    print(tweet)

    return tweet

# trying to keep functions being responsible for doing one thing
def send_tweet(tweet):
    api = create_twitter_api()
    logger.info('Sending tweet')

    api.update_status(status=tweet)
