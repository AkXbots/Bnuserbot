import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "25591955")) #optional
API_HASH = getenv("API_HASH", "190867151075b43a1d0ffb1213b16c7d") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID","5940604852"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://te.legra.ph/file/2ac1c953d54544cc79dda.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT","✘ Ραρα υѕєявσт ✘

❏ νєяѕισи: 2.1
├• υρтιмє: 0:00:06
├• ρутнσи: 3.9.7
├• ρуяσgяαм: 2.0.59
├• ѕυρρσят: Click
├• ¢нαииєℓ: Click
└• яєρσ: Click")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP","-1001870868564")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "Lowda lele")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAtMsyf7OEjLn7PuwSytr248NbTqtWNOOfNQ2XwykioXG998bkUq8MhREQL4vwedj7Kt4IWG1wNpaTio1Idej5aKEOKbNGNaH5CFbpIy65pqA8Gm_aiZsNAsYt6ESvFknNyyAZM7iYIvpWJq6wFzVlLLxem3JbeQx31dj2sVzUL1D-TqY7936EpesK1Hqo2Ut3iWLGFZu7EOmJsUvVbQraiZQKmAX9wH-ANkTz1oVXwDChHBvBelLdwJ3GXPaVgY53TmrgWz3fphakmZkP9FQR_cBsRQ-Y3aTlJjf3T_6QjHVhOOvJCYW_KTILOfRs8_81yMXNpDvedmYqVEs0DywpjwAAAAF2DKVvAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
