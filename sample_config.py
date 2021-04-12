import os


class Config(object):
    TOKEN = os.environ.get("TG_BOT_TOKEN", "1790025412:AAHZWT4L3J8d204oLSw9cfd5Mb2_99cA0vs")

    API_ID = int(os.environ.get("APP_ID", "2888382")

    API_HASH = os.environ.get("API_HASH", "908a8a13c87a6c1899f6e788a05d3d0d")
