'''
This contains the configuration and setup for the tweet function, it references environmental variables for the key & secret
'''

import tweepy
import os
import logging

from tweepy.api import API
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# this will create the tweepy twitter api including establishing the authentication
def create_twitter_api():

    #below are the auth details for the Twitter account that the bot tweets from. The actual details have been stored in a .env file and referenced here. If you are using this project, you will either need to create your own .env file or replace the strings like "TWITTER_API_KEY" etc with your own credentials
    api_key = os.getenv('TWITTER_API_KEY')
    api_secret = os.getenv('TWITTER_API_SECRET')
    access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    
    except Exception as err:
        logger.error('Error creating Twitter API, check credentials', exc_info=True)
        raise err
    
    logger.info('Twitter API created successfully')

    return api