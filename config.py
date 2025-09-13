import os


class Config(object):
    API_HASH = os.environ.get("cb3d60057fce5975e57b08a50cf57ed3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    TELEGRAM_API = os.environ.get("21551509")
    OWNER = os.environ.get("7123837674")
    OWNER_USERNAME = os.environ.get("BruceJaat")
    PASSWORD = os.environ.get("PASSWORD")
    DATABASE_URL = os.environ.get("mongodb+srv://Yashds:yashds@yashds.xzuhxvo.mongodb.net/?retryWrites=true&w=majority&appName=Yashds")
    LOGCHANNEL = os.environ.get("-1002881534182")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "1_G-vq2bZA7IYbTCOdOIdoHcfJGMaPbYq")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
