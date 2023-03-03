import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID","5940604852"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://te.legra.ph/file/2ac1c953d54544cc79dda.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBlDB-XYSNjqKwetw7-xb693VK0ZJvRUTLsGsDStCISH7VYJ3CorxAg_WTpMDMo7qVbxwgjo9g-hdtmIU8iwVGlnUQEbAREr2FAx2ZtFEsLOSrVVfk4Ggs9eDIfTtf36mNuCj4tYAeilNpKRS2qxg8tf9hHGHlngVVJv-vgSrXG0O9aUU8ZlP8RzdJoRhUi_JHIFwsAk7t2cxeVVZM9_f3WqrZtGik5RvjKWoJiZHxpeDP-cu9DLZIM74YQL6mvsx6xhMnMxWCu0KEMMBij1q-AKu0bDmufwuOaoM2oJSDV-P7BxsP1DiGpUgkg6eaQ6VZmj4J_K1bWQdlvTqefQ81CAAAAAXYMpW8A")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
