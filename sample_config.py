import os

class Config(object):
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", "27317669"))

    API_HASH = os.environ.get("API_HASH", "11b88c331c5d44fde57cf91de1a2156b")    
    
    CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "Real_Pirates")

    CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "7326600267").split())
