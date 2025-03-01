# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os
from os import getenv


def get_user_list(config, key):
    with open("{}/THEElianaPROBot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 7230086  # integer value, dont use ""
    API_HASH = "93dcc19b29f53920df7f9448e22e0f91"
    TOKEN = "2045390157:AAGzQWlpD5oORRMz_CV2Qn6OqXYSHHNvjUw"  # Your Bot Token
    OWNER_ID = 2045390157  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "SAdikulWAhidSUjon" 
    BOT_ID = ""
    HEROKU_APP_NAME = ""
    SUPPORT_CHAT = "TVB_Discussion"  # Your own group for support, do not add the @
    JOIN_LOGGER = (-1001573229865)
    EVENT_LOGS = (-1001565052701)  # Logs Channel Id do not add the @
    DATABASE_URL = getenv("DATABASE_URL", "")
    MONGO_DB_URI = ""
    HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")
    DONATION_LINK = getenv("DONATION_LINK", "https://t.me/THEElianaPRO/9")

    # RECOMMENDED
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    CERT_PATH = None
    PORT = 5000
    STRICT_GBAN = True
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    TEMP_DOWNLOAD_DIRECTORY = "./"
    SPAMWATCH_API = ""
    SPAMWATCH_SUPPORT_CHAT = "SpamWatchSupport"
    

    # OPTIONAL
    ##List of id's -  (not usernames) 
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    DEMONS = get_user_list("elevated_users.json", "supports")
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    CASH_API_KEY = (
        "WVUTR9R34VAM5LE0"  # Get your API key from https://www.alphavantage.co/support/#api-key 
    )  
    TIME_API_KEY = "4LTJHD1G5ZYD" # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php 
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
