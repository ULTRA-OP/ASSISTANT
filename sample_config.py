import os


class Config(object):
    TOKEN = os.environ.get("TG_BOT_TOKEN", "1789892375:AAFEsATJh7EHwhFtsRNWJkjpPiyae4TW_cY")

    API_ID = int(os.environ.get("APP_ID", "2654773")

    API_HASH = os.environ.get("API_HASH", "d53a77f2db19fcdb81ff2b2170e93c96")
