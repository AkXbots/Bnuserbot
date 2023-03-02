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
 
STRING_SESSION1 = getenv("STRING_SESSION1", "1AZWarzQBuwZ-NO-VtCpkfP2LXM2HFTQhtxCFNUiEeIuTOKxOsQQsRNQH2Flwj8gqEdrzrqFGZ7j1Y_qcB2S3N-6Q-grFx_kevFhTz3WNSTU_Jt36hpSCfaRHmcW5xQKSvu0IWdNPfl2RRaOfMBPXNivma0n__BajaQDlfrpGkbZLHJMZitlnt817847D5w7nAE6odh_qyYWk52GNYCxM2YP50YH6br4OMqoMw-aY3mxbNoWMmk_PQe-WZ4fyKDZgTeoXo8UzMVxuzUzAYxSZNkZEuNvj1wFHs3mVU8_grHae_wA7hDCPabe-OgmjlO1xjaUR__Wc-QW-kNfSioVb62wj6honb0g= ")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
